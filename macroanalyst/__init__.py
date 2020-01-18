from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from macroanalyst.manage import db
from macroanalyst import charts
from macroanalyst.models import Country, Indicator

import pandas as pd
from fredapi import Fred
import requests
import io
import os
import re
import json

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

"""
==================================================================
Note: refer to changelog for some elaboration on proposed changes
==================================================================
""" 


# =============================
# Flask app
# =============================

from flask import Flask

def create_app():
    """
    Constructs the core application
    """
    app = Flask(__name__,
                instance_relative_config=False)
    app.config.from_object('config.Config')

    with app.app_context():

        # Import main Blueprint
        from application import routes
        app.register_blueprint(routes.main_bp)

        # Import Dash application and register it
        # with the parent Flask app
        from application.dash_app.dashboard import Add_Dash
        app = Add_Dash(app)

        return app

# Config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(os.path.abspath(os.path.dirname(__file__)), 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init Database with SQLAlchemy
db.init_app(app)

# Init Migration
migrate = Migrate(app, db)


# =============================
# Dash app
# =============================
app.app_context().push()

select = dbc.Row([
    dbc.Col(
        dbc.Nav([
            dcc.Dropdown(
                id='dropdown-countries',
                options=[{'label': item, 'value': item}
                         for item in [x.country for x in Country.query.all()]],
                value='Australia',
                style={"width": 500}
            ),
            dcc.Dropdown(
                id='dropdown-indicators',
                value='Indicators',
                style={"width": 500}
            ),
            dcc.Dropdown(
                id='dropdown-charts',
                options=[{'label': i, 'value': i}
                         for i in ("Candlesticks", "Line Chart", "Area Chart")],
                value='Line Chart',
                style={"width": 500}
            ),
        ], id="navbar-charts"
        ), width={"size": 12, "offset": 2})
])

body = html.Div(
    dbc.Row([
            dbc.Col(
                children=[charts.main_chart],
                id="main-chart-container",
            ), dbc.Col(
                children=[charts.side_chart],
                id="side-chart-container",
                className="canvas",
            )
            ],
            id="charts-container",
            className="container"
            ),
    style={'marginBottom': 50, 'marginTop': 25}
)

dash_app = dash.Dash(
    __name__,
    server=app,
    routes_pathname_prefix='/dash/',
    meta_tags=[{"name": "viewport", "content": "width=device-width"}]
)

dash_app.layout = html.Div([
    select,
    body
])

charts.initialise_charts()


@dash_app.callback(
    dash.dependencies.Output('dropdown-indicators', 'options'),
    [dash.dependencies.Input('dropdown-countries', 'value')]
)
def update_indicator_dropdown(country_name):
    return [{'label': item.code, 'value': item.code} for item in Indicator.query.filter_by(country_id=Country.query.filter_by(country=country_name).first().id).all()]


@dash_app.callback(
    [Output('main_chart', 'figure'),
     Output('side_chart', 'figure')],
    [Input('dropdown-charts', 'value'),
     Input('dropdown-countries', 'value'),
     Input('dropdown-indicators', 'value')
     ])
def update_figure(chart_type, country_name, code_name):

    country = Country.query.filter_by(country=country_name).first()
    indicator = Indicator.query.filter_by(code=code_name)

    chart = indicator.filter_by(country_id=country.id).first()
    dataframe = pd.DataFrame()

    # Load API Keys
    with open('macroanalyst/keys.json', 'r+') as f:
        api_keys = json.load(f)

    if 'stlouis' in chart.source:
        key = api_keys['fred']

        series_id = re.search('series_id=(.*)&ap', chart.source).group(1)
        fred = Fred(api_key=key)

        dataframe = pd.DataFrame(fred.get_series(series_id))

    else:
        key = api_keys['quandl']
        link = str(chart.source).replace('API_KEY', key)
        r = requests.get(link)

        dataframe = pd.read_csv(io.StringIO(r.content.decode('utf-8')))

    if len(dataframe.columns) > 1:
        print(dataframe)
        charts.df = dataframe
        charts.set_stats(chart.indicator, charts.df.columns[1])

    if chart_type == "Candlesticks" and ("Low" or "High" or "Open" or "Last") in charts.df:

        charts.main_trace['type'] = "candlestick"
        charts.main_trace['fill'] = "none"

        ohlc = {
            "low": charts.df['Low'],
            "high": charts.df['High'],
            "open": charts.df['Open'],
            "close": charts.df['Last'],
        }

        for val in ohlc:
            charts.main_trace[val] = ohlc[val]

    elif chart_type == "Area Chart":

        charts.main_trace['type'] = "lines"
        charts.main_trace['fill'] = "tozeroy"

    else:

        charts.main_trace['type'] = "lines"
        charts.main_trace['fill'] = "none"

    return [{
        'data': charts.traces,
        'layout': charts.main_layout
    }, {
        'data': charts.side_traces,
        'layout': charts.main_layout
    }]
