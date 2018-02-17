from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, ForeignKey
import os
import MySQLdb
from engine import * 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = engine
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True

db = SQLAlchemy(app)

class country(db.Model):
    country = db.Column(db.String(40))
    country_iso2 = db.Column(db.String(2))
    country_iso3 = db.Column(db.String(3))
    country_iso_num = db.Column(db.Integer, primary_key = True)
    def __init__(self, country, country_iso2, country_is03, country_iso_num):
        self.country = country
        self.country_iso2 = country_iso2
        self.country_iso3 = country_iso3
        self.country_iso_num = country_iso_num
class alias (db.Model):
    country_alias =db.Column(db.String(40), primary_key = True)
    country_iso_num = db.column(ForeignKey("country.country_iso_num"))
    def __init__ (self, country_alias, country_iso_num):
        self.country_alias = country_alias
        self.country_iso_num = country_iso_num
class state (db.Model):
    state = db.Column(db.String(40))
    state_code = db.Column(db.String(40), primary_key = True)
    def __init__ (self, state, state_code):
        self.state = state
        self.state_code = state_code
class cities (db.Model):
    city = db.Column(db.String(40))
    city_id = db.Column(db.String(40), primary_key = True)
    state_code = db.Column(ForeignKey("state.state_code"))
    def __init__(self, city, city_id):
        self.city = city
        self.city_id = city_id
class news (db.Model):
    url = db.Column(db.String(500), primary_key = True)
    country_iso_num = db.Column(db.Integer)
    state_code = db.Column(db.String(2))
    city_id = db.Column(db.Integer)
    def __init__ (self, url, country_iso_num, state_code, city_id):
        self.url = url
        self.country_iso_num = country_iso_num
        self.state_code = state_code
        self.city_id = city_id

@app.route("/")
def main():
    db.create_all()
    return render_template("index.html")


if __name__ == "__main__":
        app.run(host='0.0.0.0')
