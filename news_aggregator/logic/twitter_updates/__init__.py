from __future__ import absolute_import, print_function

from flask import Flask, request, jsonify

import configparser, logging
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy
import requests
import json
from twitter_updates.database_config import *
from twitter_updates.engine import *
from time import sleep

app = Flask(__name__)
db =SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = engine
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True

#print(engine)

#users=['759251', '1367531', '26585095', '15012486', '2442861190', '4970411']
users=['2442861190', '964922790854955008']

@app.route("/")
def main():
    #print(country.query.all())
    return 'There is nothing here'

@app.route("/twitter", methods=['POST'])
def scrape_json():


    if request.is_json:
        content = json.loads(request.get_json())
        text = content.get('text')
        user_id = content.get('user').get('id')
        status_id = content.get('id_str')
        screen_name = content.get('user').get('screen_name')
        link = 'https://twitter.com/' + screen_name + '/status/' + status_id
        print(link)
        
        #print(country.query.all())
        if content.get('place') != None:
            place = content.get('place')
            region = place.get('name')
            country_code = place.get('country_code')
            coords = place.get('bounding_box').get('coordinates')
    
            print(region)
            print(country_code)
            print(coords)
            
            curr_country = country.query.filter_by(country_iso2=country_code).first()
            print(curr_country)
            #var = news(url=content.get('entities').get('expanded_url'), countryiso2=curr_country, regionid=None, citiesid=None,)
        else:
            for word in text.split():
                print(country.query.filter_by(country_name = word).first().country_name)
                if country.query.filter_by(country_name = word).first() is not None: 
                    var = news(url=link, country_iso2=country.query.filter_by(country_name=word).first().country_iso2, region_id=None, cities_id=None)
                    print(var)
                    db.session.add(var)
                    db.session.flush()
                    db.session.commit()
    return "Ok, scraped"

class StdOutListener(StreamListener):
    def on_data(self, data):
        url = "http://127.0.0.1:5000/twitter"
        payload = json.loads(data)
        #print(payload)
        user_id = payload.get('user').get('id')
        if user_id in users:
            print(user_id)
        r = requests.post(url, json=data)
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
    stream.filter(follow=users, async=True)

if __name__ == '__main__':
    main()
