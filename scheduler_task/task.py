"""
Author: li bo
date: 2023/4/6 17:26
"""
from apscheduler.schedulers.background import BackgroundScheduler
from db.mysqlDB import db_session
import logging

aps = BackgroundScheduler()


def refresh_api_request_times():
    db_session.execute('truncate table peer.apirequestcount;')
