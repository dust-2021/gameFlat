import asyncio
from functools import wraps
from flask import request, session, redirect, current_app, render_template, url_for
from db.mysqlDB import db_session, ApiRequestCount, DeniedIP, UserPrivilege
from sqlalchemy import text
import os
import logging
from etc.globalVar import AppConfig
from typing import Callable, Dict, List, Mapping, Tuple, Any
from logging import getLogger


def session_checker(func):
    """
    wrapper to check the cookies of user.
    :param func:
    :return:
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        _user_id = session.get('user_id')
        if _user_id is None:
            return redirect(url_for('page.login'))
        result = func(*args, **kwargs)
        return result

    return wrapper


def log_writer(logger: str = 'root'):
    def _func_log_writer(func):
        """
        function execute log.
        :param func:
        :return:
        """

        @wraps(func)
        def wrapper(*args, **kwargs):
            _log = logging.getLogger(logger)
            res = func(*args, **kwargs)
            _log.info(f'{func.__name__} execute finished, args: {args}, kwargs: {kwargs}')
            return res

        return wrapper

    return _func_log_writer


def set_period_request_count(num: int = None, period: str = 'minute'):
    """
    route get request times limit from a single ip address
    :param num: max times.
    :param period: minute, hour, day, week
    :return:
    """
    if num is None:
        num = AppConfig.API_MAX_REQUEST_TIME_PER_MINUTE if period == 'minute' else 1

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
                _log = logging.getLogger('user')
                _log.warning(f'{_ip} forbidden level raise')

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


def set_privilege_check(level: int):
    """
    check user's privilege level before request
    :param level:
    :return:
    """

    def privilege_check(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            user_id = session.get('user_id')
            res = db_session.query(UserPrivilege.privilege_level).filter_by(user_id=user_id).first()

            if res[0] < level:
                return render_template('deny.html', msg='permission denied')

            result = func(*args, **kwargs)

            return result

        return wrapper

    return privilege_check


class SingleClass(type):
    singles: dict = {}

    def __call__(cls, *args, **kwargs):
        if cls.singles.get(cls) is None:
            cls.singles[cls] = super().__call__(*args, **kwargs)
            logger = getLogger('base')
            logger.info(f'\'{cls.__name__}\' single object created')
        return cls.singles[cls]
