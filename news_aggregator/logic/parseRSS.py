import feedparser
giimport os
import json


cnn_worldnews = feedparser.parse('http://rss.cnn.com/rss/cnn_world.rss')

def populate_db():
    file = open('location_data/all.csv')

    for line in file:
        print(line.split(",")[3])
    print(file);

def loop_through_news(news):
    print(news)

populate_db()
