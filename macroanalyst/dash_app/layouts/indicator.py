import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

import plotly.graph_objects as go
import pandas as pd

from ... import Country, Indicator


# ==============================
#  Econ Charting Template
# ==============================

indicators = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H2("Filters"),
                        dbc.Form([
                            dbc.FormGroup(
                                [
                                    dbc.Label("Country", html_for="country"),
                                    dcc.Dropdown(
                                        id="country",
                                        options=[{'label': item, 'value': item} for item in [x.country for x in Country.query.all()]],
                                    ),
                                    dbc.Label("Indicator", html_for="indicator"),
                                    dcc.Dropdown(
                                        id="indicator",
                                        options=[
                                            {"label": "Gross Domestic Product", "value": 1},
                                            {"label": "Manufacturing Activity", "value": 2},
                                            {"label": "Inventory Levels", "value": 3},
                                            {"label": "Retail Sales", "value": 4},
                                            {"label": "Building Permits", "value": 5},
                                            {"label": "Housing Market", "value": 6},
                                            {"label": "New Businesses", "value": 7},
                                            {"label": "Income & Wages", "value": 8},
                                            {"label": "Unemployment Rate", "value": 9},
                                            {"label": "Consumer Price Index | Inflation", "value": 10},
                                            {"label": "Currency Strength", "value": 11},
                                            {"label": "Inventory Levels", "value": 12},
                                            {"label": "Interest Rates", "value": 13},
                                            {"label": "Corporate Profits", "value": 14},
                                            {"label": "Balance of Trade", "value": 15},
                                            {"label": "Value of Commodity Substitutes to USD", "value": 16},
                                        ],
                                    ), 
                                    dbc.Label("Type", html_for="type"),
                                    dcc.Dropdown(
                                        id="type",
                                        options=[{'label': i, 'value': i} for i in ("Candlesticks", "Line Chart", "Area Chart")],
                                    ),
                                    dcc.Graph(
                                    id="chart2",
                                    style={'height': 300}
                                    )
                                ],
                                className="mt-4"
                            )
                        ])       
                    ],
                    lg=4,
                ),
                html.Hr(className="my-2"),
                dbc.Col(
                    [
                        html.H2("Economic Data"),
                        dcc.Graph(
                            id="chart1"
                        ),
                        dbc.FormGroup(
                            [
                                dbc.Label("RangeSlider", html_for="range-slider"),
                                dcc.RangeSlider(id="range-slider", min=0, max=1000, value=[400, 700]),
                            ]
                        ),
                    ]
                ),
            ]
        )
    ],
    className="mt-4",
)