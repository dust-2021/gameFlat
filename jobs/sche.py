from apscheduler.schedulers.background import BackgroundScheduler
from etc.globalVar import AppGlobal
from task import *

aps = BackgroundScheduler()



if AppGlobal.API_PROTECT:
    aps.add_job(refresh_api_request_times, trigger='cron', minute='*', second='0', replace_existing=True)