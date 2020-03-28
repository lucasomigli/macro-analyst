# =============================
#  Dash app
# =============================

import os
import dash
from dash import Dash
from dash.dependencies import Input, Output, State
import dash_table
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
from fredapi import Fred
from pyscbwrapper import SCB
import json
import requests
import io
import re

from .layouts.base import html_layout
from .layouts.index import index
from .layouts.navbar import navbar
from .layouts.indicator import indicators
from .layouts.securities import securities
from .layouts.gov_finance import gov_finance
from .layouts.bop import bop
from .layouts.trades import trades

from .. import Indicator, Country
from .. import charts

# Page layouts defined in global scope
index_page = html.Div([
    index,
])

indicators_page = html.Div([
    indicators,
])

securities_page = html.Div([
    securities,
])

gov_finance_page = html.Div([
    gov_finance,
])

bop_page = html.Div([
    bop,
])

trades_page = html.Div([
    trades,
])


def Add_Dash(server):
    """
    Creates a Dash app (using Flask at its core)
    ========================================================
    A function is used instead of global var in order to pass
    the top-level Flask app into Dash as 'server'.

    routes_pathname_prefix establishes a domain hierarchy.
    Everything below '/dashboard/' is served by Dash.
    Everything above it is served up with Flask.
    """
    external_stylesheets = [
        dbc.themes.LUX, 'https://fonts.googleapis.com/css?family=Lato',
        'https://use.fontawesome.com/releases/v5.8.1/css/all.css'
    ]
    external_scripts = ['/static/js/main.js']

    dash_app = Dash(
        server=server,
        external_stylesheets=external_stylesheets,
        external_scripts=external_scripts,
        # Establish domain hierarchy
        routes_pathname_prefix='/analyze/')

    # Silence exception to elements not existing until callback execution
    dash_app.config.suppress_callback_exceptions = True

    # =============================
    #  Front-End SPA Instantiation
    # =============================

    # Override the underlying HTML template
    dash_app.index_string = html_layout

    # Initialize callbacks before the application has finished loading
    init_callbacks(dash_app)

    dash_app.layout = html.Div([

        # Represents the URL bar. Doesn't render anything
        dcc.Location(id='url', refresh=False),

        # The following elements render in every case
        navbar,

        # Content is rendered in this element
        html.Div(id='page-content')
    ])

    # Launch Application
    return dash_app.server


# =============================
#  Callbacks
# =============================


def init_callbacks(dash_app):
    """
    This module contains various callback and nested functions.
    """
    @dash_app.callback(Output('page-content', 'children'),
                       [Input('url', 'pathname')])
    def display_page(pathname):
        """
        Essentially serves as the Dash application's routing function

        Args: pathname passed from href link objects
        Returns: Page render that correlates to respective arg parameter
        """
        if pathname == '/analyze/indicators':
            return indicators_page
        elif pathname == '/analyze/securities':
            return securities_page
        elif pathname == '/analyze/government-finance':
            return gov_finance_page
        elif pathname == '/analyze/bop':
            return bop_page
        elif pathname == '/analyze/trades':
            return trades_page
        else:
            return index_page

    # Pertains to navbar collapse on small viewports
    @dash_app.callback(
        Output("navbar-collapse", "is_open"),
        [Input("navbar-toggler", "n_clicks")],
        [State("navbar-collapse", "is_open")],
    )
    def toggle_navbar_collapse(n, is_open):
        """Preserves navbar collapse state"""
        if n:
            return not is_open
        return is_open

    # Callbacks for Indicators view

    charts.initialise_charts()

    @dash_app.callback(
        Output('indicator', 'options'),
        [Input('country', 'value'),
         Input('intermediate-value', 'children')])
    def update_indicator_dropdown(country_name, indicator_type):
        return [{
            'label': item.code,
            'value': item.code
        } for item in Indicator.query.filter_by(
            indicator_type=indicator_type).filter_by(
                country_id=Country.query.filter_by(
                    country=country_name).first().id).all()]

    @dash_app.callback(
        [Output('chart1', 'figure'),
         Output('chart2', 'figure')], [
             Input('type', 'value'),
             Input('country', 'value'),
             Input('indicator', 'value')
         ])
    def update_figure(chart_type, country_name, code_name):

        country = Country.query.filter_by(country=country_name).first()
        indicator = Indicator.query.filter_by(code=code_name)

        chart = indicator.filter_by(country_id=country.id).first()
        dataframe = pd.DataFrame()

        # Load API Keys
        with open('macroanalyst/keys.json', 'r+') as f:
            api_keys = json.load(f)

        # St Louis FRED API
        if 'stlouis' in chart.source:
            key = api_keys['fred']

            series_id = re.search('series_id=(.*)&ap', chart.source).group(1)
            fred = Fred(api_key=key)

            dataframe = pd.DataFrame(fred.get_series(series_id),
                                     columns=['Value'])
            dataframe['Date'] = dataframe.index

            frame = {'Date': dataframe['Date'], 'Value': dataframe['Value']}

            dataframe = pd.DataFrame(data=frame)

        # European Central Bank API
        elif 'ecb' in chart.source:
            link = str(chart.source)
            response = requests.get(link, headers={'Accept': 'text/csv'})

            dataframe = pd.read_csv(
                io.StringIO(response.content.decode('utf-8'))).filter(
                    ['TIME_PERIOD', 'OBS_VALUE'], axis=1)

        # Sweden SCB API
        elif 'scb.se' in chart.source:
            scb = SCB('en')
            scb.go_down('en', 'BE', 'BE0401', 'BE0401B')

            scb_data = scb.get_data()
            """
            Translate json into dataframe
            """

        # Russian iss.moex API
        elif 'iss.moex' in chart.source:
            link = str(chart.source)
            r = requests.get(link)
            df = pd.read_csv(io.StringIO(r.content.decode('utf-8')),
                             sep=';',
                             names=[
                                 'Open', 'Close', 'High', 'Low', 'Value',
                                 'Volume', 'Date', 'End'
                             ]).iloc[2:]

            df = df.sort_values(by='Date')

            frame = {
                'Date': df['Date'].astype(np.datetime64),
                'Open': df['Open'].astype('float64'),
                'Close': df['Close'].astype('float64'),
                'High': df['High'].astype('float64'),
                'Low': df['Low'].astype('float64'),
                'Value': df['Value'].astype('float64'),
            }

            dataframe = pd.DataFrame(frame)

        else:
            key = api_keys['quandl']
            link = str(chart.source).replace('API_KEY', key)
            r = requests.get(link)

            dataframe = pd.read_csv(io.StringIO(r.content.decode('utf-8')))

        if len(dataframe.columns) > 1:
            charts.df = dataframe

            charts.set_stats(chart.indicator, charts.df.columns[1])

        if chart_type == "Candlesticks" and ("Low" or "High" or "Open"
                                             or "Close") in charts.df:

            charts.main_trace['type'] = "candlestick"
            charts.main_trace['fill'] = "none"

            ohlc = {
                "low": charts.df['Low'],
                "high": charts.df['High'],
                "open": charts.df['Open'],
                "close": charts.df['Close'],
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
