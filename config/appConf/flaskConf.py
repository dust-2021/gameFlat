import json

from redis import Redis
import os
from typing import Dict, Union, Any

# ------------------
# app load config from this file if there doesn't exist a named flaskPersonalConf.py
# ------------------
NGINX_LISTEN = 80
FLASK_PORT = 5000

# udp port listen, at least 2 port, otherwise server can't check what kind of NAT the user is in.
UDP_PORT_COUNT = 5
# udp port range, 000 or '000' or '000,001,002' or '000-003'
UDP_PORT = '5001-5020'
# if this arg is True,this app will be a master app, the data will store in
# local databases. if this arg is False, the data will store in master-host app,
# and this app can not work without master app.
IS_THE_MASTER_MACHINE = True
MASTER_HOST = None
ACCEPT_FROM_MASTER = True

# if this is False, the slave app's IP must have been added in allowed list by admin user.
PUBLIC_SLAVE_MACHINE = False

SECRET_KEY = 'example'

LOGIN_FOR_SOCKETIO = False

SESSION_TYPE = 'redis'
SESSION_USE_SIGNER = True
PERMANENT_SESSION_LIFETIME = 3600 * 24 * 7

# LOG_LEVEL = 'INFO'
LOG_FILE = 'log'

APP_ADMIN_PASSWORD = ''
APP_ENV = 'development'

# protect api route, set a default value to limit a api route can be requested by an IP in a minute.
API_PROTECT = True
API_MAX_REQUEST_TIME_PER_MINUTE = 30
API_PROTECT_INFO_TABLE = {
    'minute': 'ApiRequestCount',
    'hour': 'ApiRequestCountHour',
    'day': 'ApiRequestCountDay',
    'week': 'ApiRequestCountWeek'
}

REDIS_CONFIG = {
    'host': '127.0.0.1',
    'port': 6379,
    'password': '064735'
}
# if this app is not the master app, mysql config won't use.
MYSQL_CONF = {
    'host': '127.0.0.1',
    'port': 3306,
    'username': 'root',
    'password': '064735Freedom?',
    'database': 'peer',
    'mysql_engine': 'pymysql'
}

AMQP_CONF: Union[Dict[str, Any], None] = None

if IS_THE_MASTER_MACHINE:
    SESSION_REDIS = Redis(host=REDIS_CONFIG.get('host'), password=REDIS_CONFIG.get('password'))

SMTP_CONF = {
    'email': '',
    'password': '',
    'server_host': 'smtp.163.com',
    'server_port': 25
}

SMS_CONF = {

}
