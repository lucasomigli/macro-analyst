
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

import plotly.graph_objects as go
import pandas as pd

link_style = {
    'color': 'blue',
}

index = dbc.Jumbotron(
    dbc.Container(
        [
            html.H1("Welcome", className="display-4"),
            html.P(
                "Use the links above or below to navigate to any section of the application.",
                className="lead",
            ),
            html.P(
                [
                    "Check out any number of  ",
                    dcc.Link('common economic indicators', href='/analyze/indicators', style=link_style),
                    " that provide insight into the world around us.",
                    html.Br(),
                    "Or if you'd prefer, we also provide charting for ",
                    dcc.Link('individual securities', href='/analyze/securities', style=link_style),
                    " or ",
                    dcc.Link('fixed income investment', href='/analyze/securities', style=link_style),
                    ".",
                ]
            ),
            html.Hr(className="my-2"),
            html.P(
                "This product uses the FRED® API but is not endorsed or certified by the Federal Reserve Bank of St. Louis."
            ),
        ]
    ),  
)