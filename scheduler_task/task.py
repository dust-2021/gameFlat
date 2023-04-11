"""
Author: li bo
date: 2023/4/6 17:26
"""
from apscheduler.schedulers.background import BackgroundScheduler
from db.mysqlDB import db_session
import logging
from apscheduler.triggers.base import BaseTrigger

aps = BackgroundScheduler()


def refresh_api_request_times():
    """
    定时清空api访问计数
    :return:
    """
    db_session.execute('truncate table peer.apirequestcount;')
    db_session.commit()
    db_session.close()


aps.add_job(refresh_api_request_times, )