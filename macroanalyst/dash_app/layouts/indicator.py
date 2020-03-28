import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

import plotly.graph_objects as go
import pandas as pd

from ... import Country, Indicator
from .. import dashboard

# ==============================
#  Econ Charting Template
# ==============================

default_query = Indicator.query.filter(
    Indicator.country_id == 3, Indicator.indicator_type == 'indicators')
default_indicator = default_query.filter(
    Indicator.indicator.contains('gdp')).first().indicator

print('default indicator is ', default_indicator)

indicators = dbc.Container(
    [
        dbc.Row([
            dbc.Col(
                [
                    html.H2("Filters"),
                    html.Div(id='intermediate-value',
                             style={'display': 'none'},
                             children='indicators'),
                    dbc.Form([
                        dbc.FormGroup([
                            dbc.Label("Country", html_for="country"),
                            dcc.Dropdown(id="country",
                                         options=[{
                                             'label': item,
                                             'value': item
                                         } for item in [
                                             x.country
                                             for x in Country.query.all()
                                         ]],
                                         value='United States'),
                            dbc.Label("Indicator",
                                      html_for="indicator",
                                      id='indicator_type'),
                            dcc.Dropdown(id="indicator",
                                         options=[{
                                             'label': item,
                                             'value': item
                                         } for item in [
                                             x.indicator
                                             for x in default_query.all()
                                         ]],
                                         value='Real GDP'),
                            dbc.Label("Type", html_for="type"),
                            dcc.Dropdown(
                                id="type",
                                options=[{
                                    'label': i,
                                    'value': i
                                } for i in ("Candlesticks", "Line Chart",
                                            "Area Chart")],
                            ),
                            dcc.Graph(id="chart2", style={'height': 300})
                        ],
                                      className="mt-4")
                    ])
                ],
                lg=4,
            ),
            html.Hr(className="my-2"),
            dbc.Col([
                html.H2("Economic Data"),
                dcc.Graph(id="chart1", style={'height': 600}),
            ]),
        ])
    ],
    className="mt-4",
)