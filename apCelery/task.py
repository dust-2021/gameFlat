import json
import random

from apCelery.celery_app import celery_app
import platform
import subprocess
from apCelery.smtp_tool import send_email
from etc.tools.wrapper import log_writer


@celery_app.task
def kill_process(pid: str):
    if not platform.system() != 'Linux':
        return 'FAILED'
    res = subprocess.call(f'kill -9 {pid}', shell=True)
    return res


@celery_app.task
def celery_checker():
    """
    check apCelery server status
    :return:
    """
    return 'SUCCESS'


@celery_app.task
def smtp_sender():
    pass


@celery_app.task
def python_executor():
    pass


@celery_app.task
def mysql_executor():
    pass


@celery_app.task
@log_writer('celery')
def register_email_code(email_addr: str, username: str, password_hasher: str):
    _code = random.Random().choices(population=[str(x) for x in range(10)], k=6)
    text = f'register code: {"".join(_code)}'
    send_email(text, target=email_addr)
    data = {
        'code': _code,
        'username': username,
        'password': password_hasher,
        'type': 'email'
    }
    return data


@celery_app.task
def register_sms_code(phone_num: str):
    pass


