from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor
from sqlalchemy import create_engine
import os
from etc.globalVar import AppGlobal
from jobs.task import *

if os.path.exists('config/appConf/flaskPersonalConf.py'):
    from config.appConf.flaskPersonalConf import *
else:
    from config.appConf.flaskConf import *

_engine = create_engine(
    f'mysql+{MYSQL_CONF.get("mysql_engine")}://{MYSQL_CONF.get("username")}'
    f':{MYSQL_CONF.get("password")}@{MYSQL_CONF.get("host", "127.0.0.1")}:'
    f'{MYSQL_CONF.get("port", 3306)}/{MYSQL_CONF.get("database")}', pool_size=2)

job_store = {
    'default': SQLAlchemyJobStore(engine=_engine)
}

executors = {
    'default': ThreadPoolExecutor(max_workers=5)
}

job_defaults = {
    'coalesce': False,
    'max_instances': 5
}

aps = BackgroundScheduler(job_store=job_store, executors=executors, job_defaults=job_defaults)
aps.start()
_log = logging.getLogger('base')
_log.info('apscheduler start.')

if AppGlobal.API_PROTECT:
    aps.add_job(refresh_api_request_times, trigger='cron', minute='*', second='0', replace_existing=True)
    aps.add_job(update_ip_denied, trigger='cron', day='*', hour='3', replace_existing=True)
