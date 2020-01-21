import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from fredapi import Fred

# ==============================
#  Equities Charting Template
# ==============================

import plotly.graph_objects as go
import pandas as pd

sp500 = pd.read_csv(r'data/sp500.csv')
sp500.drop(['Settle', 'Change', 'Volume', 'Previous Day Open Interest'], axis=1, inplace=True)

fig = go.Figure()

# fig.add_trace(go.Scatter(x=sp500.Date, y=sp500.Open, name="S&P Open", line_color='green'))
fig.add_trace(go.Scatter(x=sp500.Date, y=sp500.Last, name="S&P Close", line_color='darkslategrey'))

fig.update_layout(xaxis_rangeslider_visible=True)

equities = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H2("Filters"),
                        dbc.Form([
                            dbc.FormGroup(
                                [
                                    dbc.Label("Stock", html_for="country"),
                                    dcc.Dropdown(
                                        id="country",
                                        options=[
                                            {"label": "Option 1", "value": 1},
                                            {"label": "Option 2", "value": 2},
                                        ],
                                    ),
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
                        html.H2("S&P500 Closing Price (USD)"),
                        dcc.Graph(
                            id='securities-graph',
                            figure = fig
                        )
                    ]
                ),
            ]
        )
    ],
    className="mt-4"
)