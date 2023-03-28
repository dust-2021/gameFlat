from flask import Flask
from flask_session import Session
from bluePrint.webAPI.mainApp import mainApp
import os


def create_app() -> Flask:
    """
    生成app实例，读取app配置，生成session，注册蓝图
    :return: app实例
    """
    _app = Flask(__name__, template_folder='./templates', static_folder='./static')
    _app.config.from_pyfile('config/appConf/flaskConf.py')
    if os.path.exists('config/appConf/flaskPersonal.conf.py'):
        _app.config.from_pyfile('config/appConf/flaskPersonalConf.py')
    session = Session()
    session.init_app(_app)
    _app.register_blueprint(mainApp, url_prefix='/')
    return _app


app = create_app()
