from flask import Flask, json
from pymongo import MongoClient
import settings
from os import environ

USER = environ['USER']
PASS = environ['PASS']
SERVER = environ['SERVER']
DB = environ['DB']

url= 'mongodb+srv://'+ USER + ':' + PASS +'@' + SERVER + '/' + DB +'?retryWrites=true&w=majority'
client = MongoClient(url)

app = Flask(__name__)


@app.route('/')
def hello_flask():
    
    return "<h1>Hola desde la home de <u>Flask</u> :D</h1>"

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


@app.route("/api/tweets/<usuario>")
def getTweetsSinLimite(usuario):
    return "OUT OF SERVICE"
#########################
@app.route("/api/tweets/<usuario>/<limite>")
def getTweets(usuario, limite):
    
    bigdata = client['bigdata']
    tweets = bigdata['tweets']
    
    
    if limite != None and limite.isnumeric():
        limite = int(limite)
    else:
        return "Sín resultados para la búsqueda"
        
    mis_tweets = tweets.find({'in_reply_to_screen_name': usuario}).limit(limite)
    
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
  


app.run( port = 3000 , debug = True)



