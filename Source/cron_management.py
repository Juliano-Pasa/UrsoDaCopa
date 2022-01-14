"""
    This module is responsable for updating, creating, deleting jobs in a crontab file to post and retrieve tweets

    [usr] = linux user
    [action] = 'create' to create/'remove' to remove jobs related to the tweets 
    [jobs] = Do action on "p" for post/ "r" for retrieve/ "pr" for both
  
"""

import os
import sys
from crontab import CronTab

def create_jobs(usr, jobs):
    with CronTab(user=usr) as cron:

        # Tweet posting job

        if jobs != "r":
            post_command_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../Automation/post.sh")
            post_job = cron.new(command=post_command_path, comment="post_job")
            post_job.setall(1, 0, None, None, 5)

        # Tweet info retrieving job

        if jobs != "p":
            retrieve_command_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../Automation/retrieve.sh")
            retrieve_job = cron.new(command=retrieve_command_path, comment="retrieve_job")
            retrieve_job.setall('*/15', None, None, None, None)


def remove_jobs(usr, jobs):
    with CronTab(usr) as cron:

        if jobs != "r":
            cron.remove_all(comment="post_job")

        if jobs != "p":
            cron.remove_all(comment="retrieve_job")


# def update_post_job(usr):
#     with CronTab(user=usr) as cron:
#         iter = cron.find_comment("post_job")


if __name__ == "__main__":

    arg_names = ['command', 'usr', 'action', 'jobs']
    args = dict(zip(arg_names, sys.argv))

    # Missing arguments treatment

    if 'action' not in args:
        args['action'] = "create"

    if 'usr' not in args:
        args['usr'] = True

    if 'jobs' not in args:
        args['jobs'] = "pr"

    # Chosen action treatment

    if args['action'] == "create":
        create_jobs(args['usr'], args['jobs'])

    elif args['action'] == "remove":
        remove_jobs(args['usr'], args['jobs'])

    else:
        print("The action informed is not valid. You can either type \"create\" or \"remove\".")
