from app import celery
import platform
import subprocess


@celery.task
def kill_process(pid: str):
    if not platform.system() is 'Linux':
        return 'FAILED'
    res = subprocess.call(f'kill -9 {pid}', shell=True)
    return res


@celery.task
def celery_checker():
    """
    check celery server status
    :return:
    """
    return 'SUCCESS'


@celery.task
def smtp_sender():
    pass


@celery.task
def python_executor():
    pass


@celery.task
def mysql_executor():
    pass
