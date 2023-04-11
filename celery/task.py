"""
Author: li bo
date: 2023/4/6 11:03
"""
from app import celery


@celery.task
def celery_checker():
    return 'SUCCESS'


@celery.task
def smtp_sender():
    pass


@celery.task
def python_executor():
    pass
