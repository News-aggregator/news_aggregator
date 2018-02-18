from sqlalchemy import ForeignKey
from news_aggregator.engine import *
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = engine
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True

db = SQLAlchemy(app)


class country(db.Model):
    country_name = db.Column(db.String(40))
    country_iso2 = db.Column(db.String(2))
    country_iso3 = db.Column(db.String(3))
    country_iso_num = db.Column(db.Integer, primary_key = True)
    def __init__(self, country_name, country_iso2, country_iso3, country_iso_num):
        self.country_name = country_name
        self.country_iso2 = country_iso2
        self.country_iso3 = country_iso3
        self.country_iso_num = country_iso_num
class alias (db.Model):
    country_alias =db.Column(db.String(40), primary_key = True)
    country_iso2 = db.column(ForeignKey("country.country_iso2"))
    def __init__ (self, country_alias, country_iso2):
        self.country_alias = country_alias
        self.country_iso_num = country_iso2
class region (db.Model):
    region_name = db.Column(db.String(50), primary_key= True)
    country_iso2 = db.Column(ForeignKey("country.country.iso2"), primary_key = True)
    region_id = db.Column(db.Integer)
    region_code = db.Column(db.String(4))
    def __init__ (self, region_name, country_iso2, region_id, region_code):
        self.region_name = region_name
        self.country_iso2 = country_iso2
        self.region_id = region_id
        self.region_code = region_code
class cities (db.Model):
    city = db.Column(db.String(30))
    cities_id = db.Column(db.Integer)
    region_id = db.Column(ForeignKey("region.region_id"))
    latitude = db.Column(db.Float, primary_key= True)
    longitude= db.Column(db.Float, primary_key= True)
    def __init__(self, city, cities_id, region_id, latitude, longitude):
        self.city = city
        self.cities_id = cities_id
        self.region_id = region_id
        self.latitude = latitude
        self.longitude = longitude
class news (db.Model):
    url = db.Column(db.String(500), primary_key = True)
    country_iso2 = db.Column(ForeignKey("country.country_iso2"))
    region_id = db.Column(ForeignKey("region.region_id"))
    cities_id = db.Column(ForeignKey("cities.cities_id"))
    def __init__ (self, url, country_iso2, region_id, cities_id):
        self.url = url
        self.country_iso2 = country_iso2
        self.region_id=region_id
        self.cities_id = cities_id