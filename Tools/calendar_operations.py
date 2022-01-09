"""
	 This module is responsable for doing date related operations
"""

import calendar

def count_weekday(start, finish, day):
    diff = finish - start
    total = diff.days//7

    start_day = calendar.weekday(start.year, start.month, start.day)
    finish_day = calendar.weekday(finish.year, finish.month, finish.day)

    # Condition to check if the provided day is in between the start and finish weekdays
    if start_day < day < finish_day or day < finish_day < start_day or finish_day < start_day < day:
        total += 1

    return total

def clean_tweet_date(date):
    print(date)

    date_split = date.split(' ')
    print(date_split)

    return True
