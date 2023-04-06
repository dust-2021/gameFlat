"""
Author: li bo
date: 2023/3/31 10:37
"""
import os
from redis import Redis

if os.path.exists('config/appConf/flaskPersonalConf.py'):
    from config.appConf.flaskPersonalConf import REDIS_CONFIG
else:
    from config.appConf.flaskConf import REDIS_CONFIG

redis_pool = Redis(host=REDIS_CONFIG.get('host', '127.0.0.1'), password=REDIS_CONFIG.get('password'),
                   port=REDIS_CONFIG.get('port'))
