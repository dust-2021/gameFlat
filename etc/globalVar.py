import os

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

    MAX_CONNECTION: int = 500




class AppStatus:
    """

    """
    CPU_TOTAL = 0
    CPU_USED = 0
    MEMORY_TOTAL = 0
    MEMORY_USED = 0
    CONNECTED_USER = 0


    @classmethod
    def refresh_status(cls):
        pass
