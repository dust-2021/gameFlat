"""
Author: li bo
date: 2023/3/21 23:52
"""
from functools import wraps
from flask import request, session, redirect
from db.mysqlDB import db_session, ApiRequestCount
import os
import logging

if os.path.exists('config/appConf/flaskPersonalConf.py'):
    from config.appConf.flaskPersonalConf import API_PROTECT, API_MAX_REQUEST_TIME_PER_MINUTE
else:
    from config.appConf.flaskConf import API_PROTECT, API_MAX_REQUEST_TIME_PER_MINUTE


def session_checker(func):
    """
    api session检测装饰器
    :param func:
    :return:
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        _username = session.get('username')
        _password = session.get('password')
        if not _username or not _password:
            return redirect('')
        result = func(*args, **kwargs)
        return result

    return wrapper


def func_log_writer(func):
    """
    函数执行日志记录
    :param func: 执行函数
    :return:
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        _log = logging.getLogger('funcLogger')
        res = func(*args, **kwargs)
        _log.info(f'{func.__name__} execute finished.')
        return res

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

            times = db_session.query(ApiRequestCount.times, ApiRequestCount.user_id).filter_by(ip_address=_ip).first()
            if times >= num:
                return redirect('')
            result = func(*args, **kwargs)
            return result

        return wrapper

    return period_request_count
