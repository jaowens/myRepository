#! python3
# Adding a comment for demo purposes
# samplewebservicecall.py
import requests
import json
# Add this comment

url='http://www.reddit.com/user/spilcm/comments/.json'

response= requests.get(url, verify=False)

print(response.text)
