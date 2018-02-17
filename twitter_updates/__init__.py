from __future__ import absolute_import, print_function
import configparser, logging

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy

#app = Flask(__name__)

#@app.route("/")
#def hello():
#
class StdOutListener(StreamListener):
    def on_data(self, data):
        print(data)
        return True
    def on_error(self, status):
        print(status)


class TwitterUpdate():
    consumer_key=""
    consumer_secret=""

    access_token=""
    access_secret=""
   
    def __init__(self):
        
        config = configparser.ConfigParser()
        config.read('tweet.ini')
        
        print(config.sections())
        if 'twitter' in config:
            self.consumer_key = config['twitter']['consumerKey']
            self.consumer_secret = config['twitter']['consumerSecret']

            self.access_token = config['twitter']['accessToken']
            self.access_secret = config['twitter']['accessSecret']
    
        print(self.consumer_key)
        print(self.consumer_secret)
        
        print(self.access_token)
        print(self.access_secret)

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    
    api = tweepy.API(auth)

    print(api.me().name)

    listener = StdOutListener()

    stream = Stream(auth, listener)
    stream.filter(track=['RIT'])


if __name__ == '__main__':
    twitter = TwitterUpdate()
