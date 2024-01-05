from etc.globalVar import AppConfig
from ant.udp_socket import udp_listener


class Tunnel:

    def __init__(self, from_user: int, to_user: int):
        self.from_user = from_user
        self.to_user = to_user
        self.first_sid = udp_listener.udp_sid_generator(from_user)

    def first_step(self):
        pass


    def run(self):
        sid = udp_listener.udp_sid_generator()
