import dash_core_components as dcc
import pandas as pd
import numpy as np

df = pd.read_csv(
    'https://www.quandl.com/api/v3/datasets/RBA/G01.csv?api_key=VisDzHjR9F8hyHG35baj'
)

main_chart_stats = dict()
side_chart_stats = dict()


def initialise_charts():
    # Initialises dataframe with the one given.
    set_stats('trace', df.columns[1])


def set_stats(indicator_name, column):
    # Descriptive statistics and indicators
    df['%Change'] = df[column].pct_change()
    df['sma'] = df[column].rolling(10).mean()
    df['bollinger_bands_upper'] = df[column].rolling(
        30).mean() + df[column].rolling(30).std() * 2
    df['bollinger_bands_lower'] = df[column].rolling(
        30).mean() - df[column].rolling(30).std() * 2

    if 'sma' not in df and len(df.columns) > 1:
        set_stats(df.columns[1])

        main_chart_stats = dict(mean=df['sma'].mean(),
                                standard_error=df['sma'].sem(),
                                median=df['sma'].median(),
                                mode=df['sma'].mode(),
                                standard_deviation=df['sma'].std(),
                                sample_variance=df['sma'].var(),
                                kurtosis=df['sma'].kurtosis(),
                                skewness=df['sma'].skew(),
                                range=df['sma'].max() - df['sma'].min(),
                                minimum=df['sma'].min(),
                                maximum=df['sma'].max(),
                                sum=df['sma'].sum())

        side_chart_stats = dict(mean=df['%Change'].mean(),
                                standard_error=df['%Change'].sem(),
                                median=df['%Change'].median(),
                                mode=df['%Change'].mode(),
                                standard_deviation=df['%Change'].std(),
                                sample_variance=df['%Change'].var(),
                                kurtosis=df['%Change'].kurtosis(),
                                skewness=df['%Change'].skew(),
                                range=df['%Change'].max() -
                                df['%Change'].min(),
                                minimum=df['%Change'].min(),
                                maximum=df['%Change'].max(),
                                sum=df['%Change'].sum())

    date = df.iloc[:, 0]

    main_trace['name'] = indicator_name
    main_trace['x'] = date
    main_trace['y'] = df.iloc[:, 1]
    sma_trace['x'] = date
    sma_trace['y'] = df['sma']
    bbu_trace['x'] = date
    bbu_trace['y'] = df['bollinger_bands_upper']
    bbl_trace['x'] = date
    bbl_trace['y'] = df['bollinger_bands_lower']

    side_chart_main_trace['x'] = date
    side_chart_main_trace['y'] = df['%Change']
    side_chart_sma_trace['x'] = date
    side_chart_sma_trace['y'] = df['%Change'].rolling(12).mean()

    traces = set_traces()
    side_traces = set_side_traces()


traces = []
side_traces = []


def set_traces():
    traces = []
    traces.append(main_trace)
    traces.append(sma_trace)
    traces.append(bbu_trace)
    traces.append(bbl_trace)
    return traces


def set_side_traces():
    side_traces = []
    side_traces.append(side_chart_main_trace)
    side_traces.append(side_chart_sma_trace)
    return side_traces


main_trace = {
    "line": {
        "color": "rgba(31,119,180,1)",
        "fillcolor": "rgba(31,119,180,1)"
    },
    "type": "lines",
    "fill": "none",
    "xsrc": "cbarber3102:2:063aed",
    "x": "x",
    "y": "y",
    "frame": None,
    "xaxis": "x",
    "yaxis": "y2",
}

sma_trace = {
    "line": {
        "color": "#E377C2",
        "width": 1,
        "fillcolor": "rgba(214,39,40,1)"
    },
    "mode": "lines",
    "name": "Moving Average",
    "type": "scatter",
    "xsrc": "cbarber3102:2:c433fa",
    "x": "x",
    "ysrc": "cbarber3102:2:bb9887",
    "y": "y2",
    "xaxis": "x",
    "yaxis": "y2",
    "frame": None,
    "hoverinfo": "none",
}

bbu_trace = {
    "line": {
        "color": "#ccc",
        "width": 1,
        "fillcolor": "rgba(255,127,14,1)"
    },
    "mode": "lines",
    "name": "Bollinger Bands",
    "type": "scatter",
    "x": "x",
    "xsrc": "cbarber3102:2:f43241",
    "y": "y",
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
        "width": 1,
        "fillcolor": "rgba(44,160,44,1)"
    },
    "mode": "lines",
    "name": "Bollinger Bands",
    "type": "scatter",
    "x": "x",
    "xsrc": "cbarber3102:2:a46bf2",
    "y": "y",
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
        "rangeslider": {
            "visible": True
        },
        "autorange": True
    },
    "yaxis": {
        "showticklabels": False,
        "autorange": True
    },
    "yanchor": "bottom",
    "legend": {
        "x": 0.5,
        "y": 1.0,
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

side_chart_main_trace = {
    "name": "% Change",
    "type": "line",
    'x': "x",
    'y': "y",
    "yaxis": "y2",
    "line": {
        "color": "purple"
    },
    "decreasing": {
        "line": {
            "color": "red"
        }
    },
    "increasing": {
        "line": {
            "color": "green"
        }
    }
}

side_chart_sma_trace = {
    "name": "15 SMA",
    "type": "line",
    'x': "x",
    'y': "y",
    "yaxis": "y2",
    "line": {
        "color": "lightpurple",
        "width": 1,
        "fillcolor": "rgba(44,160,44,1)"
    },
    "hoverinfo": "none",
}

traces = set_traces()
side_traces = set_side_traces()

main_chart = dcc.Graph(id='main_chart',
                       figure=dict(
                           layout=main_layout,
                           data=[main_trace, sma_trace, bbu_trace, bbl_trace],
                       ),
                       config={
                           'displayModeBar': False,
                           "autosizable": True
                       })

side_chart = dcc.Graph(id='side_chart',
                       figure=dict(
                           layout=main_layout,
                           data=[side_chart_main_trace, side_chart_sma_trace]),
                       config={
                           'displayModeBar': False,
                           "autosizable": True
                       })
