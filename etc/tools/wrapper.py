from functools import wraps
from flask import request, session, redirect, current_app
from db.mysqlDB import db_session, ApiRequestCount
import os
import logging
from etc.globalVar import AppGlobal


def session_checker(func):
    """
    wrapper to check the cookies of user.
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
    function execute log.
    :param func:
    :return:
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        _log = logging.getLogger('funcLogger')
        res = func(*args, **kwargs)
        _log.info(f'{func.__name__} execute finished.')
        return res

    return wrapper


def set_period_request_count(num: int = None):
    """
    limit how many times an IP could request a route.
    :param num: max times.
    :return:
    """
    if num is None:
        num = AppGlobal.API_MAX_REQUEST_TIME_PER_MINUTE

    def period_request_count(func):
        @wraps(func)
        def wrapper(*args, **kwargs):

            if not AppGlobal.API_PROTECT:
                return func(*args, **kwargs)

            # get the real IP while using Nginx.
            _ip = request.headers.get('X-real-IP', request.remote_addr)

            times = db_session.query(ApiRequestCount.times).filter_by(ip_address=_ip, api_route=request.url).first()[0]
            if not times:
                data = ApiRequestCount(user_id=session.get('user_id'), ip_address=_ip,
                                       api_route=request.url, times=0)
                db_session.add(data)
                db_session.commit()
            elif times >= num:
                return redirect('')

            times = db_session.query(ApiRequestCount.times).filter_by(ip_address=_ip).first()[0]
            db_session.query(ApiRequestCount).filter_by(ip_address=_ip).update({'times': int(times) + 1})
            result = func(*args, **kwargs)
            db_session.commit()
            db_session.close()
            return result

        return wrapper

    return period_request_count
