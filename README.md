# Urso Da Copa
Twitter Bot that counts down to FIFA World Cup Qatar 2022 every Friday.

This project consists of a Twitter Bot that posts the same video every Friday but at different times of the day.
It then collects data about the tweet several times, and this data can be analyzed to check if posting at different hours of the day has an effect on how popular the tweet can get.

The video used is not mine.


# System information
All code is being run in a Google Cloud Platform VM.  
OS: Debian 10 Buster v20211209  
Python: 3.7.3  


# Installation
1. Create your Python virtual environment in the root folder:

```python3 -m venv name```

2. Activate your Python virtual environment

On Windows: `name/Scripts/activate`

On Linux: `source name/bin/activate`

3. Install pip

On Windows: `python3 -m pip install --upgrade pip`

On Linux: `sudo apt-get install python3-pip`

4. Install requirements

`pip install -r requirements.txt`

Add your API Keys to your environment variables
Add the root folder path to PYTHONPATH environment variable