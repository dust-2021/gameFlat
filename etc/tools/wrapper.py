from functools import wraps
from flask import request, session, redirect, current_app, render_template
from db.mysqlDB import db_session, ApiRequestCount, DeniedIP
from sqlalchemy import text
import os
import logging
from etc.globalVar import AppConfig


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
    route get request times limit from a single ip address
    :param num: max times.
    :return:
    """
    if num is None:
        num = AppConfig.API_MAX_REQUEST_TIME_PER_MINUTE

    def period_request_count(func):
        @wraps(func)
        def wrapper(*args, **kwargs):

            if not AppConfig.API_PROTECT:
                return func(*args, **kwargs)

            # get the real IP while using Nginx.
            _ip = request.headers.get('X-real-IP', request.remote_addr)

            times = db_session.query(ApiRequestCount.times).filter_by(ip_address=_ip, api_route=request.url).first()
            if times is None or len(times) == 0:
                data = ApiRequestCount(user_id=session.get('user_id'), ip_address=_ip,
                                       api_route=request.url, times=1)
                db_session.add(data)
                db_session.commit()
                return func(*args, **kwargs)

            elif times[0] >= num:
                level = db_session.query(DeniedIP.level).filter_by(ip_address=_ip).first()
                if level is None:
                    _mem = DeniedIP(ip_address=_ip, level=1)
                    db_session.add(_mem)
                    db_session.commit()
                elif level[0] < 10:
                    db_session.query(DeniedIP).filter_by(ip_address=_ip).update({'level': level[0] + 1})
                return render_template('deny.html')

            times = times[0]
            db_session.query(ApiRequestCount).filter_by(ip_address=_ip).update({'times': int(times) + 1})
            result = func(*args, **kwargs)
            db_session.commit()
            db_session.close()
            return result

        return wrapper

    return period_request_count
