from flask import Blueprint, render_template, request, jsonify, session,redirect,url_for
from tools import func
import pymysql
from data import config

auth_bp = Blueprint('auth', __name__)

@auth_bp.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        if request.method == 'POST':
            username = request.form.get('user')
            password = request.form.get('pwd')
            auth_key = request.form.get('auth_key')

        password = func.md5_hash(password)

        if not username or not password or not auth_key:
            return jsonify({'success': False, 'message': '请输入用户名、密码及邀请码'}), 400
        elif not func.check_auth_key_status(auth_key):
            return jsonify({'success': False, 'message': '邀请码无效'}), 400
        elif func.check_username_exists(username):
            return jsonify({'success': False, 'message': '该用户名已经注册'}), 400
        else:
            try:
                func.register_user(username, password, auth_key)
                return jsonify({'success': True, 'message': '注册成功'})
            except Exception as e:
                return jsonify({'success': False, 'message': f'Error occurred: {str(e)}'}), 500



@auth_bp.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['user']
        password = request.form['pwd']

    password = func.md5_hash(password)
    connection = pymysql.connect(**config.init.DB_CONFIG)
    if not username or not password:
        return jsonify({'success': False, 'message': '请输入用户名及密码'}), 400
    else:
        try:
            with connection.cursor() as cursor:
                login_user_sql = "SELECT * FROM g_user WHERE username = %s AND password = %s"
                cursor.execute(login_user_sql, (username, password))
                login_data = cursor.fetchone()
                if login_data:
                    session['user'] = username
                    session['pwd'] = password
                    return jsonify({'success': True, 'message': '登录成功'})
                else:
                    return jsonify({'success': False, 'message': '用户名或密码错误'}), 400

        except Exception as e:
            connection.rollback()
            raise e
        finally:
            connection.close()

@auth_bp.route("/logout", methods=['GET', 'POST'])
def logout():
    if 'user' not in session or 'pwd' not in session:
        return redirect(url_for('login'))
    session.clear()
    return redirect(url_for('login'))