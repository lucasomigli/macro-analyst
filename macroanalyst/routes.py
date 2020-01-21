# =============================
#  Flask routes
# =============================

import os
from flask import Blueprint, render_template
from flask import current_app as app

main_bp = Blueprint('main_bp',
                    __name__,
                    template_folder='templates',
                    static_folder='static')


@main_bp.route('/')
def home():
    """ Landing Page """
    return render_template('index.html')