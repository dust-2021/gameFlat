import logging
import re
import subprocess
import os
from typing import Union, Mapping, List

if os.path.exists('config/appConf/flaskPersonalConf.py'):
    from config.appConf.flaskPersonalConf import FLASK_PORT
else:
    from config.appConf.flaskConf import FLASK_PORT


class NginxConf:

    def __init__(self):
        self.listen = 80
        self.path = 'nginx.conf'

    def add_upstream(self):
        pass

    def reload(self):
        cmd_code = ['sudo', 'service', 'nginx', 'restart', '-c', self.path]
        try:
            subprocess.run(cmd_code)
        except Exception as err:
            _log = logging.getLogger('base')
            _log.info('nginx reload failed')
