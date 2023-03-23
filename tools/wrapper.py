"""
Author: li bo
date: 2023/3/21 23:52
"""
from functools import wraps
from flask import request, session, redirect


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
            result = func(*args, **kwargs)
            return result

        return wrapper

    return period_request_count
