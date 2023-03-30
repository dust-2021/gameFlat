from flask import Flask
from flask_session import Session
from bluePrint.webAPI.mainApi import main_api
from bluePrint.webAPI.page import page_app
import os
import logging


def create_app() -> Flask:
    """
    生成app实例，读取app配置，生成session，注册蓝图
    :return: app实例
    """
    _app = Flask(__name__, template_folder='./templates', static_folder='./static')

    log = logging.getLogger('base')
    hd = logging.Handler('INFO')
    hd.setFormatter(logging.Formatter('{name} {asctime}: {levelname} -- {message}', style='{'))
    log.addHandler(hd)

    if os.path.exists('config/appConf/flaskPersonal.conf.py'):
        log.info('application start with default config.')
        _app.config.from_pyfile('config/appConf/flaskPersonalConf.py')
    else:
        log.info('application start with personal config.')
        _app.config.from_pyfile('config/appConf/flaskConf.py')
    session = Session()
    session.init_app(_app)
    _app.register_blueprint(main_api, url_prefix='/api')
    _app.register_blueprint(page_app, url_prefix='/')
    return _app


app = create_app()
