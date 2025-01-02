from flask import Blueprint, render_template,request,session,redirect,url_for
from data import config
import pymysql

# 创建 home 蓝图
home_bp = Blueprint('home', __name__)

# 获取 title 配置
title = config.init.title

# 定义 home 路由
@home_bp.route('/home',methods=['GET'])
def home():
    if 'user' not in session or 'pwd' not in session:
        return redirect(url_for('login'))

    id = request.args.get('id')
    username = session.get('user')
    connection = pymysql.connect(**config.init.DB_CONFIG)
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    try:
        sql = "SELECT * FROM g_js where username = %s"
        cursor.execute(sql, (username,))
        data_js = cursor.fetchall()
    except Exception as e:
        connection.rollback()
        raise e
    finally:
        connection.close()

    if not id:
        connection = pymysql.connect(**config.init.DB_CONFIG)
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        try:
            gxss_sql = "SELECT * FROM g_content"
            cursor.execute(gxss_sql)
            content = cursor.fetchall()
        except Exception as e:
            connection.rollback()
            raise e
        finally:
            connection.close()
    else:
        connection = pymysql.connect(**config.init.DB_CONFIG)
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        try:
            name_sql = "SELECT * FROM g_js where id = %s and username = %s"
            cursor.execute(name_sql, (id, username))
            data_name = cursor.fetchone()
            if data_name:
                jm_name = data_name['jm_name']
                gxss_sql = "SELECT * FROM g_content where jm_name = %s and username = %s"
                cursor.execute(gxss_sql, (jm_name, username))
                content = cursor.fetchall()
            else:
                jm_name = ""
                content = ""
        except Exception as e:
            raise e
        finally:
            connection.close()

    return render_template('home.html', title=title, username=username, content=content, data_js=data_js)

@home_bp.route('/home/del/<int:id>',methods=['GET'])
def home_del(id):
    if 'user' not in session or 'pwd' not in session:
        return redirect(url_for('login'))
    connection = pymysql.connect(**config.init.DB_CONFIG)
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    try:

        sql = "DELETE FROM g_content WHERE id = %s"
        cursor.execute(sql, (id,))

    except Exception as e:
        connection.rollback()
        raise e
    finally:
        connection.close()
    return redirect(url_for('home.home'))