import logging
from logging.handlers import TimedRotatingFileHandler
import os

if os.path.exists('config/appConf/flaskPersonalConf.py'):
    from config.appConf.flaskPersonalConf import *
else:
    from config.appConf.flaskConf import *


# the basic logger
def logger_creator():
    log = logging.getLogger('base')
    log.setLevel(logging.INFO)
    std_handler = logging.StreamHandler()
    std_handler.setLevel(logging.INFO)
    file_handler = TimedRotatingFileHandler(LOG_FILE + '/base.log', when='D', interval=10)
    file_handler.setLevel(logging.INFO)
    fmt = logging.Formatter('%(name)s %(asctime)s: %(levelname)s -- %(message)s')
    std_handler.setFormatter(fmt)
    file_handler.setFormatter(fmt)
    log.addHandler(std_handler)
    log.addHandler(file_handler)

    # initialize function called logger
    func_log = logging.getLogger('funcLogger')
    func_log.setLevel(logging.INFO)
    handler = TimedRotatingFileHandler(LOG_FILE + '/execute.log', when='D', interval=10)
    fmt = logging.Formatter('%(name)s %(asctime)s: %(levelname)s -- %(message)s')
    handler.setFormatter(fmt)
    handler.setLevel(logging.INFO)
    func_log.addHandler(handler)

    # initialize user logger
    user_log = logging.getLogger('user')
    user_log.setLevel(logging.INFO)
    handler = TimedRotatingFileHandler(LOG_FILE + '/user.log', when='D', interval=10)
    fmt = logging.Formatter('%(name)s %(asctime)s: %(levelname)s -- %(message)s')
    handler.setFormatter(fmt)
    handler.setLevel(logging.INFO)
    user_log.addHandler(handler)

    # initialize celery logger
    user_log = logging.getLogger('celery')
    user_log.setLevel(logging.INFO)
    handler = TimedRotatingFileHandler(LOG_FILE + '/celery.log', when='D', interval=10)
    fmt = logging.Formatter('%(name)s %(asctime)s: %(levelname)s -- %(message)s')
    handler.setFormatter(fmt)
    handler.setLevel(logging.INFO)
    user_log.addHandler(handler)


logger_creator()
