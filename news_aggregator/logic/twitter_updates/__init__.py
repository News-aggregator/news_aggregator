from __future__ import absolute_import, print_function

from flask import Flask, request, jsonify

import configparser, logging
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy
import requests

from time import sleep

app = Flask(__name__)

@app.route("/")
def main():
    return 'Hello Fuck Face'

@app.route("/twitter", methods=['POST'])
def scrape_json():
    print(request.is_json)
    #if request.is_json():
    #    print('Received JSON:')
    #    print(request.get_json())
    #else:
    #    print('NO FUCKING JSON')
    return 'fuck you'

class StdOutListener(StreamListener):
    def on_data(self, data):
        r = requests.post('http://127.0.0.1:5000/twitter', data = {'key':'value'})
        return True
    def on_error(self, status):
        print(status)
    
class TwitterUpdate():
    consumer_key=""
    consumer_secret=""

    access_token=""
    access_secret=""
    
    config = configparser.ConfigParser()
    config.read('tweet.ini')
    
    if 'twitter' in config.sections():
        consumer_key = config['twitter']['consumerKey']
        consumer_secret = config['twitter']['consumerSecret']
            
        access_token = config['twitter']['accessToken']
        access_secret = config['twitter']['accessSecret']
        
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    
    api = tweepy.API(auth)

    listener = StdOutListener()

    stream = Stream(auth, listener)
    stream.filter(track=['RIT Tigers'], async=True)

if __name__ == '__main__':
    main()
