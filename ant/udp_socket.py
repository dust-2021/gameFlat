import json
import socket
import uuid
from db.redisConn import udp_redis
import os
import multiprocessing

if os.path.exists('config/appConf/flaskPersonalConf.py'):
    from config.appConf.flaskPersonalConf import UDP_PORT, UDP_PORT_COUNT
else:
    from config.appConf.flaskConf import UDP_PORT, UDP_PORT_COUNT


def udp_sid_generator(user_id: int):
    sid = uuid.uuid4()
    udp_redis.set(str(user_id), value=sid, ex=60)
    return sid


def udp_sid_judge(user_id: int, upd_msg: bytes) -> bool:
    data = json.loads(upd_msg.decode())
    sid = data.get('sid')
    if sid is None:
        return False

    true_sid = udp_redis.getdel(str(user_id))
    if true_sid != sid:
        return False
    return True


def create_udp_socket_listen(port: int):
    soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        pass
    except socket.SO_ERROR as err:
        pass
