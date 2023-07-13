import json
import os
import sys
from typing import Mapping


class Config:
    BACKEND = f'redis://:064735@localhost:6379/2'
    BROKER = f'redis://:064735@localhost:6379/1'
    INCLUDE = [os.path.abspath('apCelery/task.py')]

    smtp_config: Mapping = json.loads(os.environ.get('smtp_config', '{}'))
    SMTP_SERVER_HOST = smtp_config.get('server_host')
    SMTP_SERVER_PORT = smtp_config.get('server_port')
    SMTP_EMAIL_ADDRESS = smtp_config.get('email')
    SMTP_EMAIL_PASSWORD = smtp_config.get('password')
