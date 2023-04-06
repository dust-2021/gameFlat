"""
Author: li bo
date: 2023/3/21 23:52
"""
import sys
from functools import wraps
from flask import request, session, redirect
from db.mysqlDB import db_session, ApiRequestCount
from db.redisConn import redis_pool
import os
if os.path.exists('config/appConf/flaskPersonalConf.py'):
    from config.appConf.flaskPersonalConf import API_PROTECT, API_MAX_REQUEST_TIME_PER_MINUTE
else:
    from config.appConf.flaskConf import API_PROTECT, API_MAX_REQUEST_TIME_PER_MINUTE


def session_checker(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        session.get('token')
        result = func(*args, **kwargs)
        return result

    return wrapper


def set_period_request_count(num: int):
    """
    周期内访问限制
    :param num: 限制数
    :return:
    """
    def period_request_count(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            _ip = request.headers.get('X-real-IP', request.remote_addr)
            times = db_session.query(ApiRequestCount.times).filter(ip_address=_ip)

            result = func(*args, **kwargs)
            return result

        return wrapper

    return period_request_count
