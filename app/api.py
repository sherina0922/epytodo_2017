##
## EPITECH PROJECT, 2018
## epytodo_2017
## File description:
## api controller
##

from app import *
from app.models import *
from flask import *
import datetime

class API(object):

    def __init__(self, app, conn):
        self.app = app
        self.conn = conn
        self.user = User(app, conn)
        self.task = Task(app, conn)

    def user_create(self, username, password):
        ret = {}
        if not username.isalnum():
            ret['error'] = "internal error"
        else:
            if self.user.exists(username):
                ret['error'] = "account already exists"
            else:
                if not username and not password:
                    ret['error'] = "internal error"
                else:
                    self.user.create(username, password)
                    ret['result'] = "account created"
        return json.dumps(ret)

    def user_login(self, username, password):
        ret = {}
        if not username and not password:
            ret['error'] = "login or password does not match"
        else:
            if not self.user.exists(username):
                ret['error'] = "login or password does not match"
            elif not self.user.check_password(username, password):
                ret['error'] = "login or password does not match"
            else:
                session['username'] = username
                session['id'] = self.user.get_id(username)
                ret["result"] = "signin successful"
        return json.dumps(ret)

    def user_logout(self):
        ret = {}
        session.pop('username', None)
        session.pop('id', None)
        ret['result'] = "signout successful"
        return json.dumps(ret)

    def task_create(self, title):
        if session['username']:
            ret = {}
            self.task.create_task(session['id'], title)
        return json.dumps(ret)

    def task_get_all(self, user_id):
        ret = {}
        if self.user.exists_id(user_id):
            result = self.task.get_tasks_by_user_id(user_id)
            ret['result'] = result
        else:
            ret['error'] = "user doesn't exists"
        return json.dumps(ret)
