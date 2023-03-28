"""
Author: li bo
date: 2023/3/21 23:30
"""

SECRET_KEY = ''
SESSION_TYPE = 'redis'
SESSION_USE_SIGNER = True
PERMANENT_SESSION_LIFETIME = 3600


REDIS_CONFIG = {
    'host': '127.0.0.1',
    'port': 6379,
    'password': None
}

MYSQL_CONF = {
    'host': '127.0.0.1',
    'port': 3306,
    'username': 'root',
    'password': None,
    'database': None,
    'mysql_engine': 'pymysql'
}
APP_ADMIN_PASSWORD = '064735'
APP_ENV = 'development'

