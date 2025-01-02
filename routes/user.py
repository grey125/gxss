from flask import Blueprint, render_template,request,session,redirect,url_for
from data import config
import pymysql

# 创建 home 蓝图
user_bp = Blueprint('user', __name__)

# 获取 title 配置
title = config.init.title

# 定义 home 路由
@user_bp.route('/user',methods=['GET'])
def user():
    if 'user' not in session or 'pwd' not in session:
        return redirect(url_for('login'))

    username = session.get('user')
    connection = pymysql.connect(**config.init.DB_CONFIG)
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    try:
        sql = "SELECT * FROM g_js where username = %s"
        cursor.execute(sql,(username,))
        data_js = cursor.fetchall()
    except Exception as e:
        connection.rollback()
        raise e
    finally:
        connection.close()
    return render_template('user.html', title=title, username=username, data_js=data_js)
