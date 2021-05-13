# -*- coding: utf-8 -*-
"""
Created on Thu May 13 20:10:13 2021

@author: EANT
"""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_flask():
    
    return "Hola desde la home de Flask :D"

app.run( port = 3000 )