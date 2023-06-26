import logging
from sqlalchemy import text
from db.mysqlDB import db_session, DeniedIP, ApiRequestCount
from etc.tools.wrapper import func_log_writer
from etc.globalVar import AppConfig


@func_log_writer
def refresh_api_request_times():
    """
    clear all api request time-count table.
    :return:
    """
    db_session.execute(text(f'truncate table {ApiRequestCount.__tablename__}'))
    db_session.commit()
    db_session.close()

@func_log_writer
def update_ip_denied():
    """
    turn down all ip denied level if level lt 10
    :return:
    """
    db_session.execute(text(f'update {DeniedIP.__tablename__} set level = level -1 where level < 10'))
    db_session.commit()
    db_session.close()


@func_log_writer
def reload_nginx():
    pass
