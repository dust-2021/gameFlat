import os

if os.path.exists('config/appConf/flaskPersonalConf.py'):
    from config.appConf.flaskPersonalConf import *
else:
    from config.appConf.flaskConf import *


class AppConfig:
    """
    global variable
    """
    SECRET_KEY = SECRET_KEY
    #
    IS_THE_MASTER_MACHINE = IS_THE_MASTER_MACHINE
    #
    MASTER_HOST = MASTER_HOST
    #
    API_PROTECT = API_PROTECT
    #
    API_MAX_REQUEST_TIME_PER_MINUTE = API_MAX_REQUEST_TIME_PER_MINUTE

    PEER_ROOM = list()
    DISABLE_IP = list()
    GLOBAL_ROOM_LIST = []
