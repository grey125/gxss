from flask import Flask
from data import config
from routes import register_routes
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

app = Flask(__name__, template_folder=os.path.join(project_root,'templates'), static_folder=os.path.join(project_root,'static'))
app.secret_key = config.init.SECRET_KEY
app.permanent_session_lifetime = config.init.SESSION_LIFETIME

# 注册路由
register_routes(app)

def start(port=None):
    app.run(host='0.0.0.0', port=port, debug=True)
