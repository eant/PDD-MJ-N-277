# -*- coding: utf-8 -*-
"""
Created on Thu May 13 20:10:13 2021

@author: EANT
"""
from flask import Flask, json

app = Flask(__name__)

@app.route('/')
def hello_flask():
    
    return "Hola desde la home de Flask :D"

########################
@app.route("/users")
def usersTwitter():
    users = [
        { 'name' : 'smessina_' },
        { 'name' : 'eanttech' },
        { 'name' : 'TinchoLutter' },
        { 'name' : 'bitcoinArg' }
    ]
    
    response = app.response_class(response = json.dumps(users), status = 200, mimetype = "application/json")
    
    return response


app.run( port = 3000, host = "0.0.0.0" )





