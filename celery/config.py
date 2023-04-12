"""
Author: li bo
date: 2023/3/31 10:10
"""
import os

class Config:

    BACKEND = None
    BROKER = None
    INCLUDE = [os.path.abspath('task.py')]
