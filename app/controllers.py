##
## EPITECH PROJECT, 2018
## epytodo_2017
## File description:
## controllers file
##

from app import *
from app.models import *
from flask import render_template

user = User()

class Controller(object):

    def index_action(self):
        ##user.user_exists("cyril")
        return render_template("index.html")

    def fraise(self):
        print("bite")

class UserController(object):

    def bite(self):
        Controller().fraise()