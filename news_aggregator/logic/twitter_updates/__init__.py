from __future__ import absolute_import, print_function
import configparser, logging

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy

class StdOutListener(StreamListener):
    #def on_data(self, data):
    #    print(data)
    #    return True
    def on_error(self, status):
         print(status)
    def on_status(self, status):
        print(status.text)

class TwitterUpdate():
    consumer_key=""
    consumer_secret=""

    access_token=""
    access_secret=""
    
    config = configparser.ConfigParser()
    config.read('tweet.ini')
    
    print(config.sections()) 
    
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
    stream.filter(track=['RIT'], async=True)

if __name__ == '__main__':
    twitter = TwitterUpdate()
