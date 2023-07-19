import asyncio
import json
import logging
import re
import socket
import time
import uuid
from typing import Union
from etc.tools.error_handler import AppError
from db.redisConn import udp_redis
import os
import threading

if os.path.exists('config/appConf/flaskPersonalConf.py'):
    from config.appConf.flaskPersonalConf import UDP_PORT, UDP_PORT_COUNT
else:
    from config.appConf.flaskConf import UDP_PORT, UDP_PORT_COUNT


class UdpListener:
    """
    create udp listen
    """

    def __init__(self, port: Union[str, int], bind: str = '0.0.0.0', process_size: int = UDP_PORT_COUNT):
        self.port = None
        self.bind = bind
        self.process_size = None
        self.listened_count = 0

        if isinstance(port, int):
            self.port = [port]
            self.process_size = 1

        elif isinstance(port, str) and re.match(r'^(\d+)-(\d+)$', port) is not None:
            _s, _e = re.match(r'^(\d+)-(\d+)$', port).groups()
            self.port = [x for x in range(int(_s), int(_e) + 1)]
            self.process_size = process_size

        else:
            raise AppError('check your udp port config')

    @staticmethod
    def udp_sid_generator(user_id: int):
        """
        create a sid for udp request
        :param user_id:
        :return:
        """
        sid = uuid.uuid4()
        udp_redis.set(str(user_id), value=sid, ex=60)
        return sid

    @staticmethod
    def udp_sid_judge(user_id: int, upd_msg: bytes) -> bool:
        data = json.loads(upd_msg.decode())
        sid = data.get('sid')
        if sid is None:
            return False

        true_sid = udp_redis.getdel(str(user_id))
        if true_sid != sid:
            return False
        return True

    def listen(self, port: int):
        """
        udp listener get a byte jsonify data.
         {"user_id": int, "sid": str}
        :param port:
        :return:
        """
        soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        _log = logging.getLogger('base')

        try:
            soc.bind((self.bind, port))
            self.listened_count += 1

            _log.info(f'UDP listened port: {port}')
            while True:
                data = soc.recv(1024)
                data = json.loads(data.decode())
                user_id = data.get('user_id')
                sid = data.get('sid')
                if self.udp_sid_judge(user_id, sid):
                    pass
                time.sleep(1)

        except socket.error as err:
            _log.info(f'port: {port} listen failed: {err}')
            soc.close()
        finally:
            pass

    def run(self):
        while self.listened_count <= self.process_size and len(self.port) > 0:
            _port = self.port.pop(0)
            th = threading.Thread(target=self.listen, args=(_port,), daemon=True)
            th.start()


udp_listener = UdpListener(UDP_PORT)
