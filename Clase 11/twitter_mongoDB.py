import tweepy
import json
import pprint
from pymongo import MongoClient

claves = open(r'C:\Users\gonza\Documents\Trabajo\EANT\Python\PDP\EANT-PDP-0-MODELO\5_NoSQL\claves.txt')
keys = [clave.strip('\n') for clave in claves]
consumer_key = keys[0]
consumer_secret = keys[1]
access_token = keys[2]
access_token_secret = keys[3]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
cliente = MongoClient("mongodb://localhost:27017")
bd = cliente['bigdata']
coleccion = bd['tweets']
ultimo = coleccion.find_one(sort=list({'id': -1}.items()))
if ultimo != None: ultimo_tweet = ultimo['id']
else: ultimo_tweet = None

tweets = []
contador = 1
for tweet in tweepy.Cursor(api.user_timeline, since_id = ultimo_tweet, screen_name = 'alferdez', tweet_mode = 'extended').items(2500):
   tweet_dic = tweet._json
   tweets.append(tweet_dic)
   print("tweet capturado", contador)
   contador += 1
if len(tweets) > 0:
   coleccion.insert_many(tweets)
   print("Subidos:", len(tweets), 'tweets')
else: print("No hay nuevos tweets para subir")
