from flask import Blueprint, render_template,request,session,redirect,url_for
from data import config
import pymysql
from tools import func
from datetime import datetime,timedelta

# 创建 home 蓝图
receive_bp = Blueprint('receive', __name__)

# 获取 title 配置
title = config.init.title

# 定义 home 路由
@receive_bp.route('/receive',methods=['GET'])
def receive():
    host = request.args.get('h')
    message = request.args.get('m')
    username = request.args.get('u')
    n = request.args.get('n')
    now = datetime.now()
    time_data = now.strftime("%Y-%m-%d %H:%M:%S")
    connection = pymysql.connect(**config.init.DB_CONFIG)
    try:
        with connection.cursor() as cursor:

            check_sql = "SELECT name,jm_name FROM g_js where jm_name = %s and username = %s"
            cursor.execute(check_sql, (n, username,))
            data_name = cursor.fetchone()
            if data_name:
                js_name = data_name[0]
                jm_name = data_name[1]
            else:
                js_name = ""
                jm_name = ""

            insert_xss_sql = "INSERT INTO g_content (message, host, username, time_data, js_name, jm_name) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(insert_xss_sql, (message, host, username, time_data, js_name, jm_name))
            connection.commit()
    except Exception as e:
        connection.rollback()
        raise e
    finally:
        connection.close()
