"""
Author: li bo
date: 2023/3/30 17:14
"""
from flask import Blueprint, request, render_template, session

page_app = Blueprint('page_app', __name__)


@page_app.route('/')
def index():
    return render_template('base.html')
