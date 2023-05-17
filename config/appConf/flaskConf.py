from redis import Redis

IS_THE_MASTER_MACHINE = True
MASTER_HOST = None

SECRET_KEY = 'example'
SESSION_TYPE = 'redis'
SESSION_USE_SIGNER = True
PERMANENT_SESSION_LIFETIME = 3600
LOG_LEVEL = 'INFO'
LOG_FILE = None

APP_ADMIN_PASSWORD = ''
APP_ENV = 'development'
API_PROTECT = False
API_MAX_REQUEST_TIME_PER_MINUTE = 30


REDIS_CONFIG = {
    'host': '127.0.0.1',
    'port': 6379,
    'password': None
}
MYSQL_CONF = {
    'host': '127.0.0.1',
    'port': 3306,
    'username': 'root',
    'password': '',
    'database': 'peer',
    'mysql_engine': 'pymysql'
}

SESSION_REDIS = Redis(host=REDIS_CONFIG.get('host'), password=REDIS_CONFIG.get('password'))
