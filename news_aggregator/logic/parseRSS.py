import feedparser
from news_aggregator.database_config import *

cnn_worldnews = feedparser.parse('http://rss.cnn.com/rss/cnn_world.rss')

def populate_countries_db():
    file = open('location_data/all.csv')
    for line in file:
        data = line.split(",")
        test = country(country_name= data[0], country_iso2=data[1], country_iso3=data[2], country_iso_num=data[3])
        db.session.add(test)
        db.session.flush()
        db.session.commit()
        print(test)
def populate_regions_db():
    file = open('location_data/data',  encoding = "ISO-8859-1")
    counter=0

   """for line in file:
        data = line.split(",")
        if (region.query.filter_by(region_name=data[1]).first() == None):
            counter += 1
            newRegion = region(region_id = counter, region_code=data[3], region_name=data[2], country_iso2=country.query.filter_by(country_iso2 = data[0]).first().country_iso2)
            db.session.add(newRegion)
            db.session.flush()
            db.session.commit() """


def loop_through_news(news):
    print(news)

populate_regions_db()