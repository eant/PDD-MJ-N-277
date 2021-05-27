import tweepy
import json
import pprint

claves = open(r'C:\Users\gonza\Documents\Trabajo\EANT\Python\PDP\EANT-PDP-0-MODELO\5_NoSQL\claves.txt')
keys = [clave.strip('\n') for clave in claves]
consumer_key = keys[0]
consumer_secret = keys[1]
access_token = keys[2]
access_token_secret = keys[3]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
#Mi perfil
usuario = api.me()
pprint.pprint(usuario._json)
#%%
#Otro usuario
otro_usuario = api.get_user('DrBrianMay')
pprint.pprint(otro_usuario._json)
#%%
seguidores = api.followers(screen_name = 'DrBrianMay')
for seguidor in seguidores:
   print(seguidor._json['name'])
#%%
for amigo in tweepy.Cursor(api.friends, screen_name = 'DrBrianMay').items(100):
   nombre = amigo._json['screen_name']
   print(nombre)
#%%
contador = 1
for tweet in tweepy.Cursor(api.user_timeline, screen_name = 'theweeknd', tweet_mode = 'extended').items(10):
   print(contador)
   pprint.pprint(tweet._json['full_text'])
   contador += 1
#%%
for tweet in tweepy.Cursor(api.search, q = 'Rexona', tweet_mode = 'extended').items(50):
   print(tweet._json['full_text'])
