from flask import Blueprint, request, session, redirect, render_template
from etc.tools.wrapper import session_checker, set_period_request_count

nat_api = Blueprint('nat_api', __name__)


@session_checker
def start_nat_tunel():
    """

    :return:
    """
    user_id = session.get('user_id')
    data = request.json

