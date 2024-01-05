import logging
import re
import subprocess
import os
from typing import Union, Mapping, List

from etc.globalVar import AppConfig


class UpStream:

    def __init__(self, name: str, proxy_type: str = None):
        self.name = name
        self.proxy_type = proxy_type
        self.servers: List[Mapping] = []

    def add_server(self, host: str, weight: int = None):
        s = {
            'name': None,
            'host': host,
            'weight': weight
        }
        self.servers.append(s)

    def __repr__(self):
        servers_fmt = ';\n'.join([f'server {x}' for x in self.servers])
        return 'upstream %s {\n%s;\n%s\n}' % (
            self.name, '' if self.proxy_type is None else self.proxy_type, servers_fmt)


class Stream:

    def __init__(self):
        pass


class Server:
    def __init__(self):
        pass


class NginxConf:

    def __init__(self):
        self.listen = AppConfig.NGINX_LISTEN
        self.path = os.path.abspath('nginx.conf')

    def add_upstream(self):
        pass

    def reload(self):
        cmd_code = ['sudo', 'service', 'nginx', 'restart', '-c', self.path]
        try:
            subprocess.run(cmd_code)
        except Exception as err:
            _log = logging.getLogger('base')
            _log.info(f'nginx reload failed: {err}')
