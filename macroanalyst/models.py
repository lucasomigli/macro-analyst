from marshmallow import Schema, fields
from macroanalyst.manage import db

# Country Model


class Country(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True,
    )
    country = db.Column(db.String(100), unique=True, nullable=False)
    indicators = db.relationship('Indicator', backref='country', lazy=True)

    def __init__(self, country):
        self.country = country

    def __repr__(self):
        return '<Country %r>' % self.country


# Country Schema
class CountrySchema(Schema):
    country = fields.Str()
    indicators = fields.Str()


country_schema = CountrySchema()


# Indicators Model
class Indicator(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    indicator = db.Column(db.String(120))
    code = db.Column(db.String(120))
    source = db.Column(db.String(1000))
    country_id = db.Column(db.Integer,
                           db.ForeignKey('country.id'),
                           nullable=False)
    indicator_type = db.Column(db.String(120))

    def __init__(self, indicator, code, source, country_id, indicator_type):
        self.indicator = indicator
        self.code = code
        self.source = source
        self.country_id = country_id
        self.indicator_type = indicator_type

    def __repr__(self):
        return '<Indicator %r>' % self.indicator


# Indicators Schema
class IndicatorSchema(Schema):
    id = fields.Integer(),
    indicator = fields.String(),
    code = fields.String(),
    source = fields.String(),
    country_id = fields.Integer(),
    indicator_type = fields.String()


indicator_schema = IndicatorSchema()
