# 📈 Macro-Analyst 

## ❗️❗️ **@Luca** Proposed changes to directory are discussed below:
Future changes will be committed solely to changelog.md and appended to each PR
```md
├── 📂data
│   ├── countries
│   ├── data.md
│   └── sp500.csv
├── 📂macroanalyst
│   ├── 📂dash_app
│   │   ├── dashboard.py ───────────> [primary dash_app logic]
│   │   └── 📂layouts ─────────────> [one of each file is invoked for every page view]
│   │   │   ├── base.py
│   │   │   ├── index.py ───────────> [SPA landing page]
│   │   │   ├── indicator.py ───────> [plotly charting with callbacks to APIs]
│   │   │   ├── navbar.py ──────────> [invoked for each page]
│   │   │   ├── page_not_found.py ──> [future 404 template]
│   │   │   └── stocks.py ──────────> [plotly charting with callbacks to APIs]
│   ├── 📂static
│   │   ├── 📂css
│   │   │   └── master.css
│   │   ├── 📂img
│   │   │   └── bg-masthead.jpg
│   │   ├── 📂js
│   │   │   └── creative.min.js
│   │   ├── 📂scss
│   │   └── 📂vendor
│   ├── 📂templates
│   │   └── index.html ────> [landing page template]
│   ├── __init__.py ───────> [primary flask_app logic]
│   ├── charts.py ─────────> [held over from initial clone; will incorporate]
│   ├── models.py
│   └── routes.py ─────────> [refactored for separation of concerns]
├── changelog.md
├── config.py ─────────────> [primary config for flask_app logic]
├── README.md
├── requirements.txt
├── start.sh ──────────────> [script for launching on eventual deployment]
└── wsgi.py ───────────────> [run.py in another life. wsgi by convention]
```
## ❗️❗️ **@Luca** Changelog and Reasoning

Core application logic can be found in directory `/application`.

Within that directory is a sub-directory called `/dash_app`, which is a separate module containing logic for the Dash application.
This structure seems most logical given that the Dash application is contained within Flask.

## Routes.py

Because the entry point to the application now comes through Flask, `routes.py` has the flexibility to serve up anything we want.

As you can tell, I did quite a bit of refactoring. Because Dash extends Flask, every time you make a Dash app (which we want--particularly for SPA functionality) you're creating a new Flask app. Plotly is a for-profit company so they restrict the `app` namespace through Dash. This has the effect of creating a sandbox inside of which you are restricted unless you've paid for their enterprise version. I hope you can see why this might be an issue. If we wanted to implement:
- Authentication
- Mail functionality
- Custom static assets

Essentially, what I've done, after relying heavily on the [following article](https://hackersandslackers.com/plotly-dash-with-flask/), is instantiate Dash inside of the existing Flask server instance and only calling on it when the route is requested (which is '0.0.0.0/dashboard' in this instance but can be changed arbitrarily. See `dash_app/dashboard.py`, line 34). This gives Dash control to all sub-domains under dashboard and allows Flask to control everything else through otherwise standard means.

In this way, if we ever want to extend the application in ways that Plotly/Dash prohibits outside of their enterprise version, we can do so without restriction. For instance, incorporating user models and login/logout functionality.


## About

This project was born as a series of attempts of combining together macro economical indicators and data coming from different sources in Google Sheets. Later on, this converted into the decision of building an easily accessible and free-to-use web-app. The idea is to put together an analyser that could help traders, economists and other people to have a better understanding of macro economical activity in specific countries. This way, people could benefit in both their trading and understanding of changes in business cycles. 

--------------
Macro-Analyst charts country-specific economic activity downloading data from original sources. Countries selectable have a series of indicators including:
- GDP
- Stock Market Index 
- BOP
- Trades
- Commodities
- COT Report
- PMI/NMI
- Building Permits
- M2 Money Supply
- Interest Rates
- CPI/PPI
- Total Labor Force
- Government Spending/Revenue
- Bond Rates
- Central Bank Balance Sheet

Most of data is coming from:
- Quandl.com
- db.nomics.world
- bea.gov

Where missing, some data is scraped from investing.com that provides a download section for getting historical data. 

## What to work on
As for now, I do have data for these countries: Australia, United States, Europe, Great Britain, Canada, Switzerland, China, Japan, Norway, New Zealand, Russia, Sweden, South Africa. The idea is obviously to expand to more in the future. 
Generally speaking, main concepts to work on are:
- Connect to APIs and download automatically and periodically data.
- Responsive charts that change according to selection on the menu.
- Descriptice Statistics that perform directly on the underlying data.
- Selection of different indicators from top menu-bar.
- Selection of countries from top menu.
- <Addons!> Scorecarding system to identify business cycle. Choice of Recession, High Recession, Recovery, Inflation, Hyper-Inflation. <Addons!>

Libraries we will be using:
- Django for the web app itself.
- Pandas for reading csv/xlsx, creating graphs and performing descriptive statistics
- Matplotplib for charting data and adding momentum indicatots (Bollinger bands, MACD, Stochastic RSI, RSI, Moving Average, Volume etc..)

Charting with Dash.
To add:
- Fix Momentum Indicators being 'reversed'. SMAs go up until last x days, whereas should be the opposite.
- Add functionality for hoovering on either charts to have visual response from other one. 
- All charts responding to time-frame resizing.  
- Add Histogram for graphing historical changes with normal distribution. 

## 🌍 Developers
People currently involved in the project:
- Keagan https://github.com/KeaganM
- Espoir https://github.com/espoirMur
- Trevor https://github.com/trevor-dev
- Tewo 