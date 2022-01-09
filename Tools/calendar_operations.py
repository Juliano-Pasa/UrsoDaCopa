"""
	 This module is responsable for doing date related operations
"""

import calendar
from datetime import datetime, timedelta, timezone

def count_weekday(start, finish, day):
    diff = finish - start
    total = diff.days//7

    start_day = calendar.weekday(start.year, start.month, start.day)
    finish_day = calendar.weekday(finish.year, finish.month, finish.day)

    # Condition to check if the provided day is in between the start and finish weekdays
    if start_day < day < finish_day or day < finish_day < start_day or finish_day < start_day < day:
        total += 1

    return total

def clean_tweet_date_for_files(date):
    # UTC to BRT timezone conversion

    date_time = datetime.strptime(date, "%a %b %d %H:%M:%S %z %Y") # Tweet datetime parsing

    # BRT timezone construction
    brt_time_delta = timedelta(hours=-3) 
    brt_timezone = timezone(brt_time_delta, "BRT")

    # Timezone conversion
    brt_date_time = date_time.astimezone(brt_timezone)

    date_time_str = str(brt_date_time.year) + "_" + str(brt_date_time.month) + "_" + str(brt_date_time.day) + "_" + str(brt_date_time.hour)

    return date_time_str