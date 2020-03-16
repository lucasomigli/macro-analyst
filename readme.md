# 📈 Macro-Analyst 

launch with `python wsgi.py`

## Directory structure:
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
## Changelog & Rationale

Core Flask application logic can be found in `__init__.py` under directory `/macroanalyst`. Within that directory is a sub-directory called `/dash_app`, which is a separate module containing logic for the Dash application.

Currently, Dash is instantiated inside of the existing Flask server and only launches when its route ('127.0.0.1/analyze') is requested, thereby launching a SPA whose routes can be changed arbitrarily. See `dash_app/dashboard.py`, line 60. This gives Dash control of all sub-domains under `analyze`. In this way, if we ever want to extend the application in ways that Plotly/Dash prohibits outside of their enterprise version, we can do so without restriction.

## About

This project was born as a series of attempts of combining together macro economical indicators and data coming from different sources in Google Sheets. Later on, this converted into the decision of building an easily accessible and free-to-use web-app. The idea is to put together an analyser that could help traders, economists and other people to have a better understanding of macro economical activity in specific countries. This way, people could benefit in both their trading and understanding of changes in business cycles. 

--------------
Macro-Analyst is an all-in-one analyser for macroeconomic data. Select a range of countries and different indicators:
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
- quandl.com
- fred.stlouisfed.org
- db.nomics.world
- bea.gov

Where missing, data is scraped from investing.com that provides a download section for selecting historical data. 

Selectable tabs are available. Once within the new window, users can choose between countries listed and work with a variety of indicators. These are going to be the major selections, divided by type (and therefore related tab).

### Indicators:
- GDP Growth
- PMI/NMI
- Consumer Sentiment/Confidence Index 
- Building Permits
- M2 Money Supply
- Interest Rates
- CPI/PPI
- Total Labor Force
- COT Report

### Securities
- Government Bonds (2Y, 5Y, 10Y, 20Y)
- Stock Market Index
- Commodities

### Government Finance:
- Debt To GDP Ratio
- Government Revenue
- Government Spending
- Interest Bill / GDP
- Liquidity Ratio and % Change
- Central Bank Balance Sheet (Quarterly)
- (Calculated) CBBS / GDP

### Balance of Payments:
These will need to be graphed on the same chart. Giving also a chance to download the original BOP source files. 
- Current Account Balance
- Capital Account Balance
- Net Errors And Omissions

### Trades Data:
- Trades Imports
- Trades Exports

## Issue Log
- Fix Investing.com links to be scraped and stored in database for quick access.
- Format .xls and .xlsx to dataframe. Create separate scripts by country.
- Fix Swedish SCB API to download .csv formatted data
- Add descriptive statistics histogram
- Divide charts by type in separate tab groups (See above)
- Fix Bollinger Bands and SMAs not showing correctly 
- Synronize date range sliders with % change chart
- Design and format BOP chart
- Design and plot Central Bank Balance Sheet
- (Ongoing) Add more countries and data

## Ideas Log
- Business cycle meter. Scorecards the level of inflation/deflation currently present in the analysed country
- Business idea

Libraries used:
- flask 🌶
- dash/plotly 📊
- pandas 🐼
- SQLAlchemy 🧪

## 🌍 Developers
People currently involved in the project:
- Keagan https://github.com/KeaganM
- Espoir https://github.com/espoirMur
- Trevor https://github.com/trevor-dev
- Tewo 
