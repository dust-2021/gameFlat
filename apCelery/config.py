import json
import logging
import os
import sys
from typing import Mapping
import log

if os.path.exists('config/appConf/flaskPersonalConf.py'):
    from config.appConf.flaskPersonalConf import *
else:
    from config.appConf.flaskConf import *


class Config:
    BACKEND = f'redis://:{REDIS_CONFIG.get("password")}@{REDIS_CONFIG.get("host")}:{REDIS_CONFIG.get("port")}/2'
    BROKER = f'redis://:{REDIS_CONFIG.get("password")}@{REDIS_CONFIG.get("host")}:{REDIS_CONFIG.get("port")}/1'
    INCLUDE = ['apCelery.task']

    smtp_config: Mapping = SMTP_CONF
    SMTP_SERVER_HOST = smtp_config.get('server_host')
    SMTP_SERVER_PORT = smtp_config.get('server_port')
    SMTP_EMAIL_ADDRESS = smtp_config.get('email')
    SMTP_EMAIL_PASSWORD = smtp_config.get('password')
