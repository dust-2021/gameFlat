from flask import session, request, Blueprint
from etc.globalVar import app_status

local_api = Blueprint('local_api', __name__)

