import os

class Config:

    BACKEND = f'redis://:064735@localhost:6379/2'
    BROKER = f'redis://:064735@localhost:6379/1'
    INCLUDE = [os.path.abspath('task.py')]
