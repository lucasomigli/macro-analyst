import dash_core_components as dcc
import pandas as pd
import numpy as np

df = pd.read_csv('macroanalyst/data/sp500.csv')

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

traces = []


def set_traces():
    temp = []
    temp.append(main_trace)
    temp.append(sma_trace)
    temp.append(bbu_trace)
    temp.append(bbl_trace)

    return temp


main_trace = {
    "name": "S&P 500 Index",
    "line": {
        "color": "rgba(31,119,180,1)",
        "fillcolor": "rgba(31,119,180,1)"
    },
    "type": "lines",
    "fill": "none",
    "xsrc": "cbarber3102:2:063aed",
    "x": df['Date'],
    "y": df['Settle'],
    "frame": None,
    "xaxis": "x",
    "yaxis": "y2",
    "low": df['Low'],
    "lowsrc": "cbarber3102:2:e2cfd6",
    "high": df['High'],
    "highsrc": "cbarber3102:2:9a3f4a",
    "open": df['Open'],
    "opensrc": "cbarber3102:2:911643",
    "close": df['Last'],
    "closesrc": "cbarber3102:2:248515",
}

sma_trace = {
    "line": {
        "color": "#E377C2",
        "width": 0.5,
        "fillcolor": "rgba(214,39,40,1)"
    },
    "mode": "lines",
    "name": "Moving Average",
    "type": "scatter",
    "xsrc": "cbarber3102:2:c433fa",
    "x": df['Date'],
    "ysrc": "cbarber3102:2:bb9887",
    "y": df['sma'],
    "xaxis": "x",
    "yaxis": "y2",
    "frame": None,
    "hoverinfo": "none",
}

bbu_trace = {
    "line": {
        "color": "#ccc",
        "width": 0.5,
        "fillcolor": "rgba(255,127,14,1)"
    },
    "mode": "lines",
    "name": "Bollinger Bands",
    "type": "scatter",
    "x": df['Date'],
    "xsrc": "cbarber3102:2:f43241",
    "y": df['bollinger_bands_upper'],
    "ysrc": "cbarber3102:2:ea92fd",
    "frame": None,
    "xaxis": "x",
    "yaxis": "y2",
    "legendgroup": "Bollinger Bands",
    "hoverinfosrc": "cbarber3102:2:edb3e3",
    "hoverinfo": "none",
    "legendgroup": "Bollinger Bands"
}

bbl_trace = {
    "line": {
        "color": "#ccc",
        "width": 0.5,
        "fillcolor": "rgba(44,160,44,1)"
    },
    "mode": "lines",
    "name": "Bollinger Bands",
    "type": "scatter",
    "x": df['Date'],
    "xsrc": "cbarber3102:2:a46bf2",
    "y": df['bollinger_bands_lower'],
    "ysrc": "cbarber3102:2:9b1710",
    "frame": None,
    "xaxis": "x",
    "yaxis": "y2",
    "hoverinfo": "none",
    "showlegend": False,
    "legendgroup": "Bollinger Bands"
}

main_layout = {
    "xaxis": {
        "title": "Date",
        "domain": [0, 1],
        "rangeslider": {"visible": False},
        "autorange": True
    },
    "yaxis": {
        "domain": [0, 1],
        "showticklabels": False,
        "autorange": True
    },
    "legend": {
        "x": 0.3,
        "y": 0.9,
        "yanchor": "bottom",
        "orientation": "h"
    },
    "margin": {
        "b": 40,
        "l": 60,
        "r": 10,
        "t": 25
    },
    "hovermode": "closest",
    "showlegend": True,
}

traces = set_traces()

main_chart = dcc.Graph(
    id='main_chart',
    figure=dict(
        layout=main_layout,
        data=[main_trace, sma_trace, bbu_trace, bbl_trace],
    ),
    config={'displayModeBar': False, "autosizable": True}
)

side_chart = dcc.Graph(
    id='side_chart',
    figure=dict(
        layout=main_layout,
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
    ),
    config={'displayModeBar': False, "autosizable": True}
)
