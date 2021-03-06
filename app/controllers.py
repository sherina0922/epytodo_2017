# -*- coding: utf-8 -*-
##
## EPITECH PROJECT, 2018
## epytodo_2017
## File description:
## controllers file
##

from app import *
from app.models import *
from app.api import *
from flask import *
import datetime

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
        self.api = API(app, conn)

    def register_action(self, request):
        username = request.form['username']
        password = request.form['password']
        result = self.api.user_create(username, password)
        flash(json.loads(result))
        return redirect(url_for('route_home'))

    def signin_action(self, request):
        username = request.form['username']
        password = request.form['password']
        result = self.api.user_login(username, password)
        flash(json.loads(result))
        return redirect(url_for('route_home'))

    def signout_action(self, request):
        result = self.api.user_logout()
        flash(json.loads(result))
        return redirect(url_for('route_home'))

class UserController(object):

    def __init__(self, app, conn):
        self.app = app
        self.conn = conn
        self.api = API(app, conn)

    def view_user_info_action(self):
        count = 0
        tasks_wait = 0
        tasks_done = 0
        tasks_in_pr = 0
        tasks = self.api.task_get_all(session['id'])
        tasks = json.loads(tasks)
        count = len(tasks['result'])
        for task in tasks['result']:
            if task[4] == "not started":
                tasks_wait += 1
            elif task[4] == "in progress":
                tasks_in_pr += 1
            elif task[4] == "done":
                tasks_done += 1
        return render_template("profile.html", tasks_done=tasks_done, tasks_in_pr=tasks_in_pr, tasks_wait=tasks_wait, tasks_count=count)

    def view_user_all_task_action(self):
        tasks = self.api.task_get_all(session['id'])
        tasks = json.loads(tasks)
        utc = datetime.datetime.utcnow()
        return render_template("profile_tasks.html", tasks_list=tasks['result'], utc=utc, current_date=str(datetime.datetime.strftime(utc, "%A %d %b %Y, à %H:%S")))

    def view_user_special_task_action(self, task_id):
        task = None
        result = self.api.task_get_by_id(task_id)
        result = json.loads(result)
        if 'error' in result:
            flash(result)
        else:
            task = result['result']
        return render_template("view_task.html", task=task)

    def update_task_action(self, request, task_id):
        title = request.form['title']
        status = request.form['status']
        begin = request.form['begin']
        end = request.form['end']
        print(request.form)
        ##result = self.api.task_update(task_id, title, status, begin, end)
        ##flash(json.loads(result))
        return redirect(url_for('route_user_all_task'))

    def create_task_action(self, request):
        title = request.form['title']
        begin = request.form['begin']
        end = request.form['end']
        status = request.form['status']
        result = self.api.task_create(title, begin, end, status)
        ##print(result)
        flash(json.loads(result))
        return redirect(url_for('route_user_all_task'))

    def delete_task_action(self, request, id):
        result = self.api.task_delete(id)
        flash(json.loads(result))
        return redirect(url_for('route_user_all_task'))
