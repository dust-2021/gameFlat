import os

class Config:

    BACKEND = None
    BROKER = None
    INCLUDE = [os.path.abspath('task.py')]
