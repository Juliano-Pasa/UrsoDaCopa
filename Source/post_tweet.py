"""
    This module is responsable for posting all tweets
""" 

import sys
from datetime import date

sys.path.append('./')
from Tools.calendar_operations import count_weekday
from Tools.api_authentication import auth_api

# Steps to determine how many of a certain weekday are within two dates 

d1 = date(year=2022, month=11, day=21)
d2 = date.today()

fridays = count_weekday(d2, d1, 4) # Monday = 0, Tuesday = 1, ..., Friday = 4, ..., Sunday = 6

tweet_text = f"Ainda faltam {fridays} sexta-feiras para a copa do mundo!"

api = auth_api() #tweepy api

media = api.media_upload("Media/main-vid.mp4")
media_id = media.media_id

api.update_status(status=tweet_text, media_ids=[media_id])
