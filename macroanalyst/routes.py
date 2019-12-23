from flask import render_template, url_for, flash, redirect
from macroanalyst import app
from macroanalyst.models import Country, Indicator


@app.route("/")
def index():
    return render_template('home.html')


@app.route('/main')
def main():
    return render_template('main.html')


@app.route('/dash/<name>')
def update_chart(name):
    return dict(
        indicator=Indicator.query.filter_by(country=name)
    )