"""
	 This module is responsable for doing the twitter api authentication
"""

from tweepy import OAuthHandler, API

def get_keys():

	keys = {}

	keys['consumer_key'] 		= "xxxxxxxxxxxxx" # Read this from somewhere
	keys['consumer_secret'] 	= "xxxxxxxxxxxxx" # Read this from somewhere
	keys['access_token'] 		= "xxxxxxxxxxxxx" # Read this from somewhere
	keys['access_token_secret'] = "xxxxxxxxxxxxx" # Read this from somewhere

	return keys

def auth_api():

    keys = get_keys()

    auth = OAuthHandler(keys['consumer_key'], keys['consumer_secret'])
    auth.set_access_token(keys['access_token'], keys['access_token_secret'])

    return API(auth)
