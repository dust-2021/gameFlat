from redis import Redis

# if this arg is True,this app will be a master app, the data will store in
# local databases. if this arg is False, the data will store in master-host app,
# and this app can not work without master app.
IS_THE_MASTER_MACHINE = True
MASTER_HOST = None

SECRET_KEY = 'example'

LOGIN_FOR_SOCKETIO = False

SESSION_TYPE = 'redis'
SESSION_USE_SIGNER = True
PERMANENT_SESSION_LIFETIME = 3600

# LOG_LEVEL = 'INFO'
LOG_FILE = 'log'

APP_ADMIN_PASSWORD = ''
APP_ENV = 'development'

# if this arg is True, some api can not be request more than 30 times per minute,
# if more than 30 times, the request IP will be baned.
API_PROTECT = False
API_MAX_REQUEST_TIME_PER_MINUTE = 30

REDIS_CONFIG = {
    'host': '127.0.0.1',
    'port': 6379,
    'password': None
}
# if this app is not the master app, mysql config won't use.
MYSQL_CONF = {
    'host': '127.0.0.1',
    'port': 3306,
    'username': 'root',
    'password': '',
    'database': 'peer',
    'mysql_engine': 'pymysql'
}
if IS_THE_MASTER_MACHINE:
    SESSION_REDIS = Redis(host=REDIS_CONFIG.get('host'), password=REDIS_CONFIG.get('password'))
