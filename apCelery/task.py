import random

from .celery_app import celery_app
import platform
import subprocess
from .smtp_tool import send_email


@celery_app.task
def kill_process(pid: str):
    if not platform.system() is 'Linux':
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
def register_email_code(email_addr: str):
    _code = random.Random().choices(population=[str(x) for x in range(10)], k=6)
    text = f'register code: {"".join(_code)}'
    send_email(text, target=email_addr)
    return _code


@celery_app.task
def register_sms_code(phone_num: str):
    pass

