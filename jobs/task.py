import logging
from sqlalchemy import text
from db.mysqlDB import db_session, DeniedIP, ApiRequestCount
from etc.tools.wrapper import log_writer
from etc.globalVar import AppConfig, AppStatus


@log_writer('funcLogger')
def refresh_api_request_times(table_name: str = AppConfig.API_PROTECT_INFO_TABLE.get('minute')):
    """
    clear all api request time-count table.
    :return:
    """
    db_session.execute(text(f'truncate table {table_name}'))
    db_session.commit()
    db_session.close()


@log_writer('funcLogger')
def update_ip_denied():
    """
    turn down all ip denied level if level lt 10
    :return:
    """
    db_session.execute(text(f'update {DeniedIP.__tablename__} set level = level -1 where level < 10'))
    db_session.commit()
    db_session.close()


@log_writer('funcLogger')
def reload_nginx():
    pass
