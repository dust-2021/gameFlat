from flask import Flask, request
from flask_session import Session

from bluePrint.webAPI.mainApi import main_api
from bluePrint.webAPI.page import page_app
import os
import logging
from ant.socketApi import soc


def create_app() -> Flask:
    """
    generate a Flask app object with a config file, initial app session,
    and register blueprint.
    :return: app
    """
    _app = Flask(__name__, template_folder='./templates', static_folder='./static')

    _log = logging.getLogger('base')

    # load config
    if os.path.exists('config/appConf/flaskPersonalConf.py'):
        _log.info('application start with personal config.')
        _app.config.from_pyfile('config/appConf/flaskPersonalConf.py')
    else:
        _log.info('application start with default config.')
        _app.config.from_pyfile('config/appConf/flaskConf.py')

    # register blueprint
    _app.register_blueprint(main_api, url_prefix='/api')
    _app.register_blueprint(page_app, url_prefix='/')

    # master machine config
    if _app.config.get('IS_THE_MASTER_MACHINE'):
        from bluePrint.master.masterMainApi import master

        _app.register_blueprint(master, url_prefix='/master')

        session = Session()
        session.init_app(_app)
    return _app


app = create_app()
soc.init_app(app)

if __name__ == '__main__':
    soc.run(app, host='0.0.0.0', debug=True)
