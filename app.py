from bottle import Bottle, route, run, abort, static_file, error, response, request, post, redirect
from mako.template import Template
from utils.db import db
import datetime
import time
from utils.auth import abort_if_not_authorized


@post('/login')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        response.set_cookie("account", username, secret='spiss-project')
        redirect("/main")
    else:
        redirect("/")


@post('/register')
def do_register():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if db.users.find_one({"username": username}):
        abort(500, "User already exists")
    else:
        db.users.save({
            "username": username,
            "password": password
        })


# Define routes
@route('/')
def hello():
    print("/")
    template = Template(filename='views/index.html')
    return template.render()


@route('/index')
def index():
    print("/index")
    template = Template(filename='views/index.html')
    return template.render()

@route('/main')
def notes():
    print("/main")
    abort_if_not_authorized()
    template = Template(filename='views/main.html')
    return template.render()


# Security - restrict view templates
@route('/views/<template>')
def restricted(template):
    print("Unauthorized attempt to accesss template " + template)
    abort(401, "Sorry, access denied.")


@route('/logout')
def logout():
    print("/index")
    response.set_cookie("no", "nope", secret='nope')
    template = Template(filename='views/index.html')
    return template.render()

def check_login(username, password):
    users = list(db.users.find({"username": username, "password": password}))
    return len(users) > 0


# Define modules/routes
import services.main


# Serve static content


run(host='0.0.0.0', port=8080, debug=True)
