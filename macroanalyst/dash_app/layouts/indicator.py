import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

import plotly.graph_objects as go
import pandas as pd

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
                                        options=[
                                            {"label": "Option 1", "value": 1},
                                            {"label": "Option 2", "value": 2},
                                        ],
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
                            figure={"data": [{
                                "x": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], 
                                "y": [1, 4, 9, 11, 26, 24, 25, 32, 45, 67, 110, 112, 134, 123, 127, 113, 120, 135]}
                            ]}
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
        ),
        html.Hr(className="my-2"),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H2("Heading"),
                        html.P(
                            """This is sample text"""
                        ),
                    ]
                )
            ]
        )
    ],
    className="mt-4",
)