import json
import logging
import os
import sys
from typing import Mapping
import log

_log = logging.getLogger('celery')
if os.path.exists('config/appConf/flaskPersonalConf.py'):
    _log.info('celery start with personal config')
    from config.appConf.flaskPersonalConf import *
else:
    _log.info('celery start with default config')
    from config.appConf.flaskConf import *

del _log


class Config:
    BACKEND = f'redis://:{REDIS_CONFIG.get("password")}@{REDIS_CONFIG.get("host")}:{REDIS_CONFIG.get("port")}/2'
    # BROKER = f'redis://:{REDIS_CONFIG.get("password")}@{REDIS_CONFIG.get("host")}:{REDIS_CONFIG.get("port")}/1'
    BROKER = 'amqp://guest:guest@127.0.0.1:5672/'
    INCLUDE = ['apCelery.task']
    TIME_ZOO = 'Asia/Shanghai'

    smtp_config: Mapping = SMTP_CONF
    SMTP_SERVER_HOST = smtp_config.get('server_host')
    SMTP_SERVER_PORT = smtp_config.get('server_port')
    SMTP_EMAIL_ADDRESS = smtp_config.get('email')
    SMTP_EMAIL_PASSWORD = smtp_config.get('password')
