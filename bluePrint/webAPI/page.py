"""
Author: li bo
date: 2023/3/30 17:14
"""
from flask import Blueprint, request, render_template, session, redirect
from tools.wrapper import session_checker

page_app = Blueprint('page_app', __name__)


@page_app.route('/')
def index():
    return render_template('base.html')


@page_app.route('/login')
@session_checker
def login():
    return redirect('/')
