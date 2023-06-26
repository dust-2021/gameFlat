from flask import Blueprint, render_template, redirect
from etc.tools.wrapper import set_period_request_count

page_app = Blueprint('page_app', __name__)


@page_app.route('/')
@set_period_request_count()
def index():
    return render_template('base.html')


@page_app.route('/login')
@set_period_request_count()
def login():
    return render_template('login.html')


@page_app.route('/denied')
def denied():
    return render_template('deny.html')
