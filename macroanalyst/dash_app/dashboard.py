# =============================
#  Dash app
# =============================

from dash import Dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

from .layout import html_layout


def Add_Dash(server):
    """
    Creates a Dash app (using Flask at its core)
    ========================================================
    A function is used instead of global var in order to pass
    the top-level Flask app into Dash as 'server'.

    routes_pathname_prefix establishes a domain hierarchy.
    Everything below '/dashboard/' is served by Dash.
    Everything above it is served up with Flask.
    """
    external_stylesheets = ['/static/css/styles.css',
                            'https://fonts.googleapis.com/css?family=Lato',
                            'https://use.fontawesome.com/releases/v5.8.1/css/all.css']
    external_scripts = ['/static/js/main.js']

    dash_app = Dash(server=server,
                    external_stylesheets=external_stylesheets,
                    external_scripts=external_scripts,
                    # Establish domain hierarchy
                    routes_pathname_prefix='/dashboard/')

    # Override the underlying HTML template
    dash_app.index_string = html_layout

    # Create Dash Layout
    dash_app.layout = html.Div(
    #   children=get_datasets(),
        id='dash-container'
    )

    return dash_app.server

""" Example dataset import """
# def get_datasets():
#     """Return previews of all CSVs saved in /data directory."""
#     p = Path('.')
#     data_filepath = list(p.glob('data/*.csv'))
#     arr = ['This is an example Plot.ly Dash App.']
#     for index, csv in enumerate(data_filepath):
#         df = pd.read_csv(data_filepath[index]).head(10)
#         table_preview = dash_table.DataTable(
#             id='table_' + str(index),
#             columns=[{"name": i, "id": i} for i in df.columns],
#             data=df.to_dict("rows"),
#             sort_action="native",
#             sort_mode='single'
#         )
#         arr.append(table_preview)
#     return arr