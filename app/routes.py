import random

from main import another_app
from flask import request
from flask import make_response


@another_app.route("/")
def set_cookie():
    user_agent = request.headers.get('User-Agent')
    if 'Mozilla' in user_agent:
        flag_value = random.randint(1, 1000)
        response = make_response('<h1>Hello World</h1>')
        response.set_cookie('flag', str(flag_value))
        return response


@another_app.route('/page1')
def page1():
    return '<h1>It is page1</h1>'


@another_app.route('/page2/<name>')
def page2(name):
    return '<h2>Hello, {}</h2>'.format(name)
