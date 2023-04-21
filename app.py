from flask import Flask
from flask_session import Session

import log
from bluePrint.webAPI.mainApi import main_api
from bluePrint.webAPI.page import page_app
import os
import logging
from ant.socket_conn import soc


def create_app() -> Flask:
    """
    生成app实例，读取app配置，生成session，注册蓝图
    :return: app实例
    """
    _app = Flask(__name__, template_folder='./templates', static_folder='./static')

    _log = logging.getLogger('base')

    if os.path.exists('config/appConf/flaskPersonalConf.py'):
        _log.info('application start with personal config.')
        _app.config.from_pyfile('config/appConf/flaskPersonalConf.py')
    else:
        _log.info('application start with default config.')
        _app.config.from_pyfile('config/appConf/flaskConf.py')

    session = Session()
    session.init_app(_app)
    _app.register_blueprint(main_api, url_prefix='/api')
    _app.register_blueprint(page_app, url_prefix='/')
    return _app


app = create_app()
soc.init_app(app)

if __name__ == '__main__':
    soc.run(host='0.0.0.0', debug=True)
