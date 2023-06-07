from db.mysqlDB import ApiRequestCount, DeniedIP, User, UserPrivilege, db_session
from flask import session, request, redirect, Blueprint

mysqlDB = Blueprint('mysqlDB', __name__)


@mysqlDB.route('/request_times', methods=['POST'])
def request_times():
    """
    request json:
        {'ip': ip address}
    response json:
        {}
    :return:
    """
    data = request.json
    times = db_session.query(ApiRequestCount.times).filter_by(ip_address=data.get('ip'), api_route=request.url).first()
    if times is None:
        pass
