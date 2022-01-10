"""
	 This module is responsable for doing the twitter api authentication
"""
import os
from tweepy import OAuthHandler, API

def get_keys():

	keys = {}

	keys['consumer_key'] 		= os.environ.get('CONSUMER_KEY')
	keys['consumer_secret'] 	= os.environ.get('CONSUMER_KEY_SECRET')
	keys['access_token'] 		= os.environ.get('ACCESS_TOKEN')
	keys['access_token_secret'] = os.environ.get('ACCESS_TOKEN_SECRET')

	print(keys)

	return keys

def auth_api():

    keys = get_keys()

    auth = OAuthHandler(keys['consumer_key'], keys['consumer_secret'])
    auth.set_access_token(keys['access_token'], keys['access_token_secret'])

    return API(auth)
