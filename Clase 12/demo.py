# -*- coding: utf-8 -*-
from flask import Flask, json
from pymongo import MongoClient

USER = 'belloma'
PASS = 'admin1234'
SERVER = 'datacluster.sggre.mongodb.net'
DB = 'bigdata'
url= 'mongodb+srv://'+ USER + ':' + PASS +'@' + SERVER + '/' + DB +'?retryWrites=true&w=majority'
client = MongoClient(url)

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

########################
@app.route("/users/<path>")
def searchUsers(path):
    if path == "people":
        return "Aca va un JSON de personas..."
    elif path == "company":
        return "Aca va un JSON de empresas..."
    else:
        return "Upps... no puedo mostrar lo que estás pidiendo :P"


#########################
@app.route("/api/tweets")
def getTweets():
    
    bigdata = client['bigdata']
    tweets = bigdata['tweets']
    
    mis_tweets = tweets.find()
    
    res = []
    for tweet in mis_tweets:
        
        el_tweet = {
            'id': tweet['id_str'],
            'user': tweet['in_reply_to_screen_name'],
            'txt': tweet['full_text']
        }
        res.append(el_tweet)
        
    response = app.response_class(response = json.dumps(res), status = 200, mimetype = "application/json")
    
    return response
  


app.run( port = 3000 )



