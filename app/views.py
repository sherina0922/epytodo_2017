##
## EPITECH PROJECT, 2018
## epytodo_2017
## File description:
## vienws file
##

from app import *

## Index page
@app.route('/', methods = ['GET'])
@app.route('/index', methods = ['GET'])

def route_home():
    return Controller(app).index_action()

## User pages
@app.route('/user/<username>', methods = ['POST'])

def route_add_user(username):
    return "User added !\n"
