"""
this application must configurate a redis-server.
db-0: flask session.
db-1: apCelery.
db-2: apCelery result.
db-3: mem cache.
db-4: local socketio.
db-5: master socketio.
"""
import os
from redis import Redis

if os.path.exists('config/appConf/flaskPersonalConf.py'):
    from config.appConf.flaskPersonalConf import REDIS_CONFIG
else:
    from config.appConf.flaskConf import REDIS_CONFIG

cache_redis = Redis(host=REDIS_CONFIG.get('host', '127.0.0.1'), password=REDIS_CONFIG.get('password'),
                    port=REDIS_CONFIG.get('port'), db=3)

socket_redis = Redis(host=REDIS_CONFIG.get('host', '127.0.0.1'), password=REDIS_CONFIG.get('password'),
                     port=REDIS_CONFIG.get('port'), db=4)

celery_redis = Redis(host=REDIS_CONFIG.get('host', '127.0.0.1'), password=REDIS_CONFIG.get('password'),
                     port=REDIS_CONFIG.get('port'), db=2)
