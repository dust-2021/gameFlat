from flask import Blueprint, render_template, redirect
from etc.tools.wrapper import session_checker

page_app = Blueprint('page_app', __name__)


@page_app.route('/')
def index():
    return render_template('base.html')


@page_app.route('/login')
@session_checker
def login():
    return redirect('/')


@page_app.route('/denied')
def denied():
    pass
