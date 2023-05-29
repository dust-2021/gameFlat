from apscheduler.schedulers.background import BackgroundScheduler
from db.mysqlDB import db_session
from etc.tools.wrapper import func_log_writer

aps = BackgroundScheduler()


@func_log_writer
def refresh_api_request_times():
    """
    clear all api request time-count table.
    :return:
    """
    db_session.execute('truncate table peer.apirequestcount;')
    db_session.commit()
    db_session.close()


@func_log_writer
def reload_nginx():
    pass


aps.add_job(refresh_api_request_times, )
