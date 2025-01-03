from routes.auth import auth_bp
from routes.home import home_bp
from routes.project import project_bp
from routes.js import js_bp
from routes.receive import receive_bp
from routes.user import user_bp
from flask import Flask, render_template,session,redirect,url_for
from data import config

def register_routes(app):
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(home_bp)
    app.register_blueprint(project_bp)
    app.register_blueprint(js_bp)
    app.register_blueprint(receive_bp)
    app.register_blueprint(user_bp)
    # 注册其他路由

    title = config.init.title

    @app.route('/')
    def index():
        if 'user' not in session or 'pwd' not in session:
            return redirect(url_for('login'))
        return redirect(url_for('home.home'))
    @app.route('/login')
    def login():
        return render_template('login.html', title=title, message=title)

    @app.route('/register')
    def register():
        return render_template('register.html', title=title, message=title)

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('404.html'),404

