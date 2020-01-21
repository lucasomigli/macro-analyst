from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from macroanalyst.manage import db
from macroanalyst import charts
from macroanalyst.models import Country, Indicator

import pandas as pd
from fredapi import Fred

import requests
import io
import os
import re
import json

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

"""
==================================================================
Note: refer to changelog for some elaboration on proposed changes
==================================================================
"""

# =============================
# Flask app
# =============================

def create_app():
    """
    Constructs the core application
    """
    app = Flask(__name__,
                instance_relative_config=False)
    app.config.from_object('config.Config')

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(os.path.abspath(os.path.dirname(__file__)), 'db.sqlite')
    
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Init Database with SQLAlchemy
    db.init_app(app)

    # Init Migration
    migrate = Migrate(app, db)

    with app.app_context():

        # Import main Blueprint
        from macroanalyst import routes
        app.register_blueprint(routes.main_bp)

        # Import Dash application and register it
        # with the parent Flask app
        from macroanalyst.dash_app.dashboard import Add_Dash
        app = Add_Dash(app)

        return app


