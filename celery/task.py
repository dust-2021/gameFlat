"""
Author: li bo
date: 2023/4/6 11:03
"""
from app import celery


@celery.task
def celery_checker():
    return 'SUCCESS'
