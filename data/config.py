import secrets
from datetime import timedelta

class init:
    SECRET_KEY = secrets.token_hex(16)
    SESSION_LIFETIME = timedelta(hours=12)
    DB_CONFIG = {
        'host': '192.168.2.18',
        'user': 'root',
        'password': 'root',
        'database': 'gxss',
        'charset': 'utf8mb4'
    }
    title = "GXss"

config = init()