import os

if os.path.exists('config/appConf/flaskPersonalConf.py'):
    from config.appConf.flaskPersonalConf import *
else:
    from config.appConf.flaskConf import *


class AppGlobal:
    IS_THE_MASTER_MACHINE = IS_THE_MASTER_MACHINE
    MASTER_HOST = MASTER_HOST
    PEER_ROOM = list()
    DISABLE_IP = list()
    GLOBAL_ROOM_LIST = []
