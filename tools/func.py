import hashlib
import pymysql
from data import config

def encrypt_to_hex(string):
    return string.encode('utf-8').hex()
def md5_hash(password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()
def check_auth_key_status(auth_key):
    connection = pymysql.connect(**config.init.DB_CONFIG)
    try:
        with connection.cursor() as cursor:
            check_sql = "SELECT COUNT(*) FROM g_key WHERE auth_key = %s AND status = 0"
            cursor.execute(check_sql, (auth_key,))
            count = cursor.fetchone()[0]
            return count > 0
    finally:
        connection.close()

def check_username_exists(username):
    connection = pymysql.connect(**config.init.DB_CONFIG)
    try:
        with connection.cursor() as cursor:
            check_sql = "SELECT COUNT(*) FROM g_user WHERE username = %s"
            cursor.execute(check_sql, (username,))
            count = cursor.fetchone()[0]
            return count > 0
    finally:
        connection.close()

def register_user(username, password, auth_key):
    connection = pymysql.connect(**config.init.DB_CONFIG)
    try:
        with connection.cursor() as cursor:
            insert_user_sql = "INSERT INTO g_user (username, password,auth_key) VALUES (%s, %s, %s)"
            cursor.execute(insert_user_sql, (username, password, auth_key))

            update_key_sql = "UPDATE g_key SET status = 1 WHERE auth_key = %s"
            cursor.execute(update_key_sql, (auth_key,))

            connection.commit()
    except Exception as e:
        connection.rollback()
        raise e
    finally:
        connection.close()