import socket


def send(host: str, port: int, msg: str):
    soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    soc.sendto(msg.encode(encoding='utf-8'), (host, port))


if __name__ == '__main__':
    data = {"user_id": int, "sid": str, "target_user": int}
