from flask import Blueprint, render_template,request,session,redirect,url_for
from data import config
import pymysql

# 创建 home 蓝图
project_bp = Blueprint('project', __name__)

# 获取 title 配置
title = config.init.title

# 定义 home 路由
@project_bp.route('/project',methods=['GET'])
def project():
    if 'user' not in session or 'pwd' not in session:
        return redirect(url_for('login'))

    username = session.get('user')
    connection = pymysql.connect(**config.init.DB_CONFIG)
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    try:
        gxss_sql = "SELECT * FROM g_js where username = %s"
        cursor.execute(gxss_sql,(username,))
        js_data = cursor.fetchall()
    except Exception as e:
        connection.rollback()
        raise e
    finally:
        connection.close()

    return render_template('project.html', title=title, username=username, js_data=js_data)

@project_bp.route('/project/create',methods=['GET'])
def project_create():
    if 'user' not in session or 'pwd' not in session:
        return redirect(url_for('login'))
    username = session.get('user')

    return render_template('/project_create.html', title=title, username=username)

@project_bp.route('/project/del/<int:id>',methods=['GET'])
def project_del(id):
    if 'user' not in session or 'pwd' not in session:
        return redirect(url_for('login'))

    connection = pymysql.connect(**config.init.DB_CONFIG)
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    try:
        gxss_sql = "DELETE FROM g_js WHERE id = %s"
        cursor.execute(gxss_sql, (id,))
    except Exception as e:
        connection.rollback()
        raise e
    finally:
        connection.close()
    return redirect(url_for('project.project'))