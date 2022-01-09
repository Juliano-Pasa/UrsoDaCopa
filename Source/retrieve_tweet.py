"""
    This module is responsable from retrieving tweets and their metrics
"""

import sys

sys.path.append('./')
from Tools.api_authentication import auth_api
from Tools.calendar_operations import clean_tweet_date_for_files
from Tools.file_manipulation import write_to_file

api = auth_api()

user_ID = "UrsoBrTodaSexta" # My user ID

last_tweet = api.user_timeline(user_id=user_ID, count=1, tweet_mode='extended')

tweet_id = last_tweet[0]._json['id']
tweet_date = last_tweet[0]._json['created_at']

metrics = [
        last_tweet[0]._json['favorite_count'], 
        last_tweet[0]._json['retweet_count'], 
        last_tweet[0]._json['user']['followers_count']
        ]

date_time_str = clean_tweet_date_for_files(tweet_date)

filename = date_time_str + "_" + str(tweet_id)

write_to_file(filename, metrics)