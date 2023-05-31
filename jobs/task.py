import logging

from apscheduler.schedulers.background import BackgroundScheduler
from db.mysqlDB import db_session
from etc.tools.wrapper import func_log_writer
from etc.globalVar import AppGlobal

@func_log_writer
def refresh_api_request_times():
    """
    clear all api request time-count table.
    :return:
    """
    _log = logging.getLogger('funcLogger')
    _log.info(f'task: \'refresh_api_request_times\' executed.')

    db_session.execute('truncate table peer.apirequestcount;')
    db_session.commit()
    db_session.close()


@func_log_writer
def reload_nginx():
    pass



