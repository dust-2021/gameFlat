import os
import psutil

if os.path.exists('config/appConf/flaskPersonalConf.py'):
    from config.appConf.flaskPersonalConf import *
else:
    from config.appConf.flaskConf import *


class AppConfig:
    """
    global variable, load app start config into memcache, admin user can modify these
    configs while app running.
    """
    # app secret key for session and password hash, can't modify after init.
    SECRET_KEY: str = SECRET_KEY
    #
    IS_THE_MASTER_MACHINE: bool = IS_THE_MASTER_MACHINE
    #
    MASTER_HOST: str = MASTER_HOST
    #
    ACCEPT_FROM_MASTER: bool = ACCEPT_FROM_MASTER
    #
    API_PROTECT: bool = API_PROTECT
    #
    API_MAX_REQUEST_TIME_PER_MINUTE: int = API_MAX_REQUEST_TIME_PER_MINUTE
    #
    API_PROTECT_INFO_TABLE = API_PROTECT_INFO_TABLE

    MAX_CONNECTION: int = 500

    NGINX_LISTEN = NGINX_LISTEN


class AppStatus:
    """

    """
    def __init__(self):
        pass

    @property
    def cpu_core_count(self):
        return psutil.cpu_count()

    @property
    def cpu_used(self):
        return psutil.cpu_percent()

    @property
    def mem_count(self):
        return psutil.virtual_memory()

    @property
    def connected_user_count(self) -> int:
        from db.redisConn import socket_redis
        return socket_redis.dbsize()


# global app current status store.
app_status = AppStatus()
