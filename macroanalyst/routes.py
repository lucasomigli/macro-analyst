# =============================
#  Flask routes
# =============================

"""
==================================================================
Note: refer to changelog for some elaboration on proposed changes
==================================================================
""" 

import os
from flask import Blueprint, render_template
from flask import current_app as app

main_bp = Blueprint('main_bp', __name__,
                    template_folder='templates',
                    static_folder='static')

@main_bp.route('/')
def home():
    """ Landing Page """
    return render_template('index.html')

# @main_bp.route("/")
# def index():
#     return render_template('home.html')

# @app.route('/main')
# def main():
#     return render_template('main.html')

# @app.route('/dash/<name>')
# def update_chart(name):
#     return dict(
#         indicator=Indicator.query.filter_by(country=name)
#     )
