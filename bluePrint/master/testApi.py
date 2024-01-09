import datetime
import time

from flask import session, jsonify
from flask.blueprints import Blueprint
import asyncio
from db.mysqlDB import db_session
from db.redisConn import cache_redis

test_bp = Blueprint('test', __name__)


@test_bp.route('/async/test', methods=['GET'])
def test():
    time.sleep(2)
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
