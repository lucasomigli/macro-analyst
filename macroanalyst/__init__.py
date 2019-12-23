from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from macroanalyst.manage import db
from macroanalyst import charts
import os

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output


# =============================
# Flask app
# =============================

app = Flask(__name__)

# Config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(os.path.abspath(os.path.dirname(__file__)), 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init Database with SQLAlchemy
db.init_app(app)

# Init Migration
migrate = Migrate(app, db)

from macroanalyst import routes

# =============================
# Dash app
# =============================

select = dbc.Row([
    dbc.Col(
        dbc.Nav([
            dcc.Dropdown(
                id='dropdown-countries',
                options=[{'label': i, 'value': i}
                         for i in ("United States", "United Kindom", "Australia", "Europe")],
                value='Australia',
                style={"width": 150}
            ),
            dcc.Dropdown(
                id='dropdown-indicators',
                options=[{'label': i, 'value': i}
                         for i in ("GDP", "Stock Market", "Balance Of Payments",
                                   "Trades", "Commodities", "COT Report", "PMI & NMI", "Building Permits")],
                value='GDP',
                style={"width": 150}
            ),
            dcc.Dropdown(
                id='dropdown-charts',
                options=[{'label': i, 'value': i}
                         for i in ("Candlesticks", "Line Chart", "Area Chart")],
                value='Line Chart',
                style={"width": 150}
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
    routes_pathname_prefix='/dash/'
)

dash_app.layout = html.Div([
    select,
    body
])


@dash_app.callback(
    Output('main_chart', 'figure'),
    [Input('dropdown-charts', 'value'),
     ])
def update_figure(chart_type):

    if chart_type == "Candlesticks":

        charts.main_trace['type'] = "candlestick"
        charts.main_trace['fill'] = "none"

    elif chart_type == "Area Chart":

        charts.main_trace['type'] = "lines"
        charts.main_trace['fill'] = "tozeroy"

    else:

        charts.main_trace['type'] = "lines"
        charts.main_trace['fill'] = "none"

    return {
        'data': charts.traces,
        'layout': charts.main_layout
    }
