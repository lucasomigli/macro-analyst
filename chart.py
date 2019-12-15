import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from dateutil.relativedelta import relativedelta

import pandas as pd
import numpy as np

df = pd.read_csv('data/sp500.csv')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Descriptive statistics and indicators
df['%Change'] = df['Settle'].pct_change()
df['sma'] = df['Settle'].rolling(10).mean()
df['bollinger_bands_upper'] = df['Settle'].rolling(
    30).mean() + df['Settle'].rolling(30).std() * 2
df['bollinger_bands_lower'] = df['Settle'].rolling(
    30).mean() - df['Settle'].rolling(30).std() * 2

# App layout
app.layout = html.Div([
    html.H5(children='SP500', id='main-title'),
    dcc.Graph(
        id='graph',
        figure=dict(
            layout={
                "xaxis": {"rangeselector": {
                    "x": 0,
                    "y": 0.9,
                    "font": {"size": 13},
                    "visible": True,
                    "bgcolor": "rgba(150, 200, 250, 0.4)",
                    "buttons": [
                        {
                            "step": "all",
                            "count": 1,
                            "label": "reset"
                        },
                        {
                            "step": "year",
                            "count": 1,
                            "label": "1yr",
                            "stepmode": "backward"
                        },
                        {
                            "step": "month",
                            "count": 3,
                            "label": "3 mo",
                            "stepmode": "backward"
                        },
                        {
                            "step": "month",
                            "count": 1,
                            "label": "1 mo",
                            "stepmode": "backward"
                        },
                        {"step": "all"}
                    ]
                }},
                "yaxis": {
                    "domain": [0, df['Last'].max()],
                    "showticklabels": False
                },
                "legend": {
                    "x": 0.3,
                    "y": 0.9,
                    "yanchor": "bottom",
                    "orientation": "h"
                },
                "margin": {
                    "b": 40,
                    "l": 40,
                    "r": 40,
                    "t": 40
                },
                "yaxis2": {"domain": [0.2, 0.8]},
                "plot_bgcolor": "rgb(250, 250, 250)"
            },
            data=[{
                "name": "S&P 500 Index",
                "type": "line",
                'x': df['Date'],
                'y': df['Settle'],
                "yaxis": "y2",
                "low": df['Low'],
                "high": df['High'],
                "open": df['Open'],
                "last": df['Last'],
                "line": {"color": "green"},
                "decreasing": {"line": {"color": "red"}},
                "increasing": {"line": {"color": "green"}}
            }, {
                "line": {"width": 1},
                "mode": "lines",
                "name": "Moving Average",
                "type": "scatter",
                "x": df['Date'],
                "y": df['sma'],
                "yaxis": "y2",
                "marker": {"color": "#E377C2"}
            }, {
                "name": "Volume",
                "type": "bar",
                "x": df['Date'],
                "y": df['Volume'],
                "yaxis": "y",
                "marker": {"color": "purple"}
            }, {
                "line": {"width": 1},
                "name": "Bollinger Bands",
                "type": "scatter",
                "x": df['Date'],
                "y": df['bollinger_bands_upper'],
                "yaxis": "y2",
                "marker": {"color": "lightblue"},
                "hoverinfo": "none",
                "legendgroup": "Bollinger Bands"
            }, {
                "line": {"width": 1},
                "type": "scatter",
                "x": df['Date'],
                "y": df['bollinger_bands_lower'],
                "yaxis": "y2",
                "marker": {"color": "lightblue"},
                "hoverinfo": "none",
                "showlegend": False,
                "legendgroup": "Bollinger Bands"
            }
            ]
        )
    ),
    dcc.Graph(id='change-chart',
              figure=dict(
                  layout={
                      "x": 0,
                      "y": 0.9,
                      "font": {"size": 13},
                      "visible": True,
                  },
                  data=[
                      {
                          "name": "% Change",
                          "type": "line",
                          'x': df['Date'],
                          'y': df['%Change'],
                          "yaxis": "y2",
                          "line": {"color": "purple"},
                          "decreasing": {"line": {"color": "red"}},
                          "increasing": {"line": {"color": "green"}}
                      }, {
                          "name": "15 SMA",
                          "type": "line",
                          'x': df['Date'],
                          'y': df['%Change'].rolling(15).mean(),
                          "yaxis": "y2",
                          "line": {"color": "lightpurple"}
                      }

                  ]
              )
              )
])

if __name__ == '__main__':
    app.run_server(debug=True, port=8000)
