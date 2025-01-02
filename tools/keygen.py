import random
import string
import pymysql
from data import config

# 生成随机字符串
def generate_random_string(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


# 检查字符串是否存在于数据库
def string_exists_in_db(cursor, random_string):
    check_sql = "SELECT COUNT(*) FROM g_key WHERE auth_key = %s"
    cursor.execute(check_sql, (random_string,))
    count = cursor.fetchone()[0]
    #print(f"Checking if '{random_string}' exists in the database: {count}")
    return count > 0

def main(num):
    # 连接数据库
    connection = pymysql.connect(**config.init.DB_CONFIG)

    try:
        with connection.cursor() as cursor:
            num = int(num) # 需要生成的字符串数量
            added_count = 0
            added_strings = []
            max_attempts = 1000  # 最大尝试次数，避免无限循环
            attempts = 0

            while added_count < num:
                new_string = generate_random_string()
                attempts += 1

                # 如果超过最大尝试次数，退出循环
                if attempts > max_attempts:
                    print("All possible unique strings have been generated or max attempts reached.")
                    break

                # 检查字符串是否重复
                if not string_exists_in_db(cursor, new_string):
                    insert_sql = "INSERT INTO g_key (auth_key, status) VALUES (%s, 0)"
                    cursor.execute(insert_sql, (new_string,))
                    connection.commit()
                    added_strings.append(new_string)
                    added_count += 1
                    attempts = 0  # 重置尝试计数
                    #print(f"Added: {new_string}")
                else:
                    print(f"Duplicate found: {new_string}, generating a new one.")

    except Exception as e:
        connection.rollback()
        print("An error occurred:", e)

    finally:
        connection.close()

    print("Key generation complete ["+str(num)+"]:\n"+'\n'.join(added_strings))
