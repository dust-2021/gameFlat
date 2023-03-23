"""
Author: li bo
date: 2023/3/23 11:36
"""


class Config:
    """
    默认配置
    """

    def __init__(self):
        pass

    def load(self):
        pass


class TestConfig(Config):
    """
    测试配置
    """

    def __init__(self):
        super(TestConfig, self).__init__()


class DevConfig(Config):
    """
    开发配置
    """

    def __init__(self):
        super(DevConfig, self).__init__()


class ProdConfig(Config):
    """
    生产配置
    """

    def __init__(self):
        super(ProdConfig, self).__init__()
