from etc.globalVar import AppConfig
from hashlib import sha256
from typing import Union, Mapping, Sequence, List


class Room:

    def __init__(self, name: str, ):
        self.name = name
        self.machine_ip = None
        self.uuid = None
