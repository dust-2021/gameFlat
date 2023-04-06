"""
Author: li bo
date: 2023/3/21 23:29
"""
from celery import Celery
from config import Config

celery = Celery('celery', broker='', backend='')
celery.config_from_object(Config)
