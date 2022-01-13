"""
    This module is responsable from retrieving a user's last tweet and its metrics

    [user_ID] = user's ID which tweet will be retrieved
    [write] = W to write metrics in a file / P to print the metrics

"""

import sys

from Tools.api_authentication import auth_api
from Tools.calendar_operations import clean_tweet_date_for_files, datetime_for_metrics
from Tools.file_manipulation import write_to_file

if __name__ == "__main__":

    arg_names = ['command', 'user_ID', 'write']
    args = dict(zip(arg_names, sys.argv))

    if 'user_ID' not in args:
        args['user_ID'] = "UrsoBrTodaSexta"

    if 'write' not in args:
        args['write'] = "W"

    api = auth_api() #tweepy api

    # Retrieve last tweet

    last_tweet = api.user_timeline(user_id=args['user_ID'], count=1, tweet_mode='extended')

    tweet_id = last_tweet[0]._json['id']
    tweet_date = last_tweet[0]._json['created_at']

    # Retrieve available metrics

    metrics = [
            datetime_for_metrics(),
            last_tweet[0]._json['favorite_count'], 
            last_tweet[0]._json['retweet_count'], 
            last_tweet[0]._json['user']['followers_count'],
            ]

    if args['write'] == "W":
        date_time_str = clean_tweet_date_for_files(tweet_date)
        filename = date_time_str + "_" + str(tweet_id)
        write_to_file(filename, metrics)

    else:
        print(metrics)