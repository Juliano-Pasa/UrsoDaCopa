# Urso Da Copa
Twitter Bot that counts down to FIFA World Cup Qatar 2022 every Friday.

This project consists of a Twitter Bot that posts the same video every Friday but at different times of the day.
It then collects data about the tweet several times, so this data can be analyzed to check if posting at different hours of the day has an effect on how popular the tweet can get. There are still some hardcoded numbers related to the usage of this specific bot, but there are plans to make everything editable in the future. 

The video used is not mine.


# System information
All code is being run in a Google Cloud Platform VM.  
OS: Debian 10 Buster v20211209  
Python: 3.7.3  


# Installation
To run this code, you must have Twitter API elevated access since it uses standard v1.1 endpoints and Twitter API v2. Enter this [link](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api) to know more about how to get access to Twitter's API.


Currently, the process of automating the scripts for posting and retrieving tweet information only works on Linux because it uses crontab. There are plans to make an automation for Windows in the future.


## 1. Add your API Keys and root folder path to your environment variables

- On Linux, open your .bash_profile. You can use the text editor you prefer.
```
$ nano .bash_profile 
```

- Copy this into your file with your respective keys and path
```
export CONSUMER_KEY="Your consumer key"
export CONSUMER_KEY_SECRET="Your consumer key secret"
export ACCESS_TOKEN="Your access token"
export ACCESS_TOKEN_SECRET="Your access token secret"
export PYTHONPATH=Project Main Folder Absolute Path
```

- On Windows, you can follow this [tutorial](https://www.architectryan.com/2018/08/31/how-to-change-environment-variables-on-windows-10/). Name your environment variables the same as you would in Linux.

## 2. Create your Python virtual environment in the root folder:

```
$ python3 -m venv name 
# You can use 'venv' as a name
```

## 3. Activate your Python virtual environment

```
On Windows: name/Scripts/activate

On Linux: $ source name/bin/activate
```

## 4. Install pip

```
On Windows: python3 -m pip install --upgrade pip

On Linux: $ sudo apt-get install python3-pip
```

## 5. Install requirements

```
$ pip install -r requirements.txt
```

## 6. Automate the scripts (Only on Linux)

- Launch the virtual environment from your main folder
```
$ source name/bin/activate
```
- Execute cronjob creation
```
$ cd Source
$ python3 cron_management.py your_user
```

# Fit the code to you
Currently, there is no interface to edit some parameters, so you have to do it by hand navigating through the code.

- Change Media

To change the media you upload, first move it to the [Media](Media) folder. Then, go to line 26 in [post_tweet.py](Source/post_tweet.py) and change "main-vid.mp4" to your media name.

- Change Tweet Text

To change your tweet text, go to line 20 in [post_tweet.py](Source/post_tweet.py) and type what you want in between "".  
Example: tweet_text = "I want to write this!"

- Change cronjobs (only Linux)

To change your cronjobs, go to [cron_management.py](Source/cron_management.py) and edit line 22 and/or line 29 using crontab notation. You can visit this [website](https://crontab.guru/) to understand and generate the crontab notation.