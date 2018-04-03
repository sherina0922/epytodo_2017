##
## EPITECH PROJECT, 2018
## epytodo_2017
## File description:
## controllers file
##

from app import *
from app.models import *
from flask import *

class Controller(object):

    def __init__(self, app, conn):
        self.app = app
        self.conn = conn
        self.user = User(app, conn)

    def index_action(self):
        return render_template("index.html")

class AuthController(object):
    def __init__(self, app, conn):
        self.app = app
        self.conn = conn
        self.user = User(app, conn)

    def register_action(self, request):
        username = request.form['username']
        password = request.form['password']
        if (not username.isalnum() or not password.isalnum()):
            print('invalid: Only alpha-numeric characters are allowed')
        else:
            if self.user.user_exists(username) == 1:
                print("User exists")
            else:
                if (len(username) > 0 and len(password) > 0):
                    self.user.user_create(username, password)
                else:
                    print('Invalid: you need to enter the name and the password')
        return redirect(url_for('route_home'))

    def signin_action(self, request):
        username = request.form['username']
        password = request.form['password']
        if (not username.isalnum() or not password.isalnum()):
            print('invalid: Only alpha-numeric characters are allowed')
        else:
            if ((len(username) > 0) and (len(password) > 0)):
                if (self.user.user_exists(username) == 1):
                    print("User exists")
                    session['username'] = username
                    session['id'] = 0
                    print(session['username'], session['id'])
                    return redirect(url_for('route_user_info'))
                else:
                    print("user doesn't exist")
            else:
                print('Invalid: you need to enter the name and the password')
        return redirect(url_for('route_home'))

    def signout_action(self, request):
        session.pop('username', None)
        session.pop('id', None)
        return redirect(url_for('route_home'))

class UserController(object):

    def __init__(self, app, conn):
        self.app = app
        self.conn = conn
        self.user = User(app, conn)


class TaskController(object):

    def __init__(self, app, conn):
        self.app = app
        self.conn = conn
        self.user = User(app, conn)
