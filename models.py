from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
import os

from app import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(os.path.abspath(os.path.dirname(__file__)), 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Init database application with sqlalchemy
db = SQLAlchemy(app)
# Init marshmallow schema
ma = Marshmallow(app)
# Init Migration
migrate = Migrate(app, db)


# Country Model
class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True,)
    country = db.Column(db.String(100), unique=True, nullable=False)
    indicators = db.relationship('Indicator', backref='country', lazy=True)

    def __init__(self, country):
        self.country = country

    def __repr__(self):
        return '<Country %r>' % self.country


# Country Schema
class CountrySchema(ma.Schema):
    class Meta:
        fields = ('id', 'country')


country_schema = CountrySchema()
countries_schema = CountrySchema()


# Indicators Model
class Indicator (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    indicator = db.Column(db.String(120))
    code = db.Column(db.String(120))
    source = db.Column(db.String(1000))
    country_id = db.Column(db.Integer, db.ForeignKey(
        'country.id'), nullable=False)

    def __init__(self, indicator, code, source, country_id):
        self.indicator = indicator
        self.code = code
        self.source = source
        self.country_id = country_id

    def __repr__(self):
        return '<Indicator %r>' % self.indicator


# Indicators Schema
class IndicatorSchema(ma.Schema):
    class Meta:
        fields = ('id', 'indicator', 'code', 'source', 'country_id')


indicator_schema = IndicatorSchema()
indicators_schema = IndicatorSchema()
