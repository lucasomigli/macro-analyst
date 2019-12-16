import dash
import charts
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

import pandas as pd
import numpy as np

df = pd.read_csv('data/sp500.csv')

# Descriptive statistics and indicators

df['%Change'] = df['Settle'].pct_change()
df['sma'] = df['Settle'].rolling(10).mean()
df['bollinger_bands_upper'] = df['Settle'].rolling(
    30).mean() + df['Settle'].rolling(30).std() * 2
df['bollinger_bands_lower'] = df['Settle'].rolling(
    30).mean() - df['Settle'].rolling(30).std() * 2

main_chart_stats = dict(
    mean=df['sma'].mean(),
    standard_error=df['sma'].sem(),
    median=df['sma'].median(),
    mode=df['sma'].mode(),
    standard_deviation=df['sma'].std(),
    sample_variance=df['sma'].var(),
    kurtosis=df['sma'].kurtosis(),
    skewness=df['sma'].skew(),
    range=df['sma'].max()-df['sma'].min(),
    minimum=df['sma'].min(),
    maximum=df['sma'].max(),
    sum=df['sma'].sum()
)

side_chart_stats = dict(
    mean=df['%Change'].mean(),
    standard_error=df['%Change'].sem(),
    median=df['%Change'].median(),
    mode=df['%Change'].mode(),
    standard_deviation=df['%Change'].std(),
    sample_variance=df['%Change'].var(),
    kurtosis=df['%Change'].kurtosis(),
    skewness=df['%Change'].skew(),
    range=df['%Change'].max()-df['%Change'].min(),
    minimum=df['%Change'].min(),
    maximum=df['%Change'].max(),
    sum=df['%Change'].sum()
)

main_chart = dcc.Graph(
    id='main_chart',
    figure=dict(
        layout={
            "title": "Main Chart",
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
)

side_chart = dcc.Graph(
    id='side_chart',
    figure=dict(
        layout={
            "title": "% Change",
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
