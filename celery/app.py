"""
Author: li bo
date: 2023/3/21 23:29
"""
from celery import Celery

celery = Celery('celery', broker='', backend='')
celery.config_from_object()