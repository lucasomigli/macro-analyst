## Quick note on data

Some data has direct download links from various APIs (Gov websites and more).
Other types of data include links to investing.com or BEA (or others possibly) where direct links where not found. 
Also, ost of data comes in .csv format, other times only a .xlsx or .xls file was available!

API based links (need API Key):
- Quandl
- ecb.europa.eu

Direct Links (No API key needed):
- fred.stlouisfed.org (US Federal Reserve)
- CFTC (Commodity Futures Trading Commission)
- BEA (Bureau of Economic Analysis)
- gov.uk (UK Government website)
- abs.gov.au

Websites to be scraped (NO API nor direct link available):
- Investing.com


### Country Specific Data

## United States

| Indicator | Source | Comment |
| :---         |     :---:      |          ---: |
| COT Report   | cftc.gov     | .zip expand to .xls (or get from https://www.quandl.com/data/CFTC/098662_F_L_ALL_OI-Commitment-of-Traders-U-S-DOLLAR-INDEX-ICUS-Futures-Only-Percent-of-Open-Interest-Legacy-Format-098662)  |
| Building Permits   | census.gov     | .xls file  |

## Europe

| Indicator | Source | Comment |
| :---         |     :---:      |          ---: |
| PMI   | Investing.com | Scrape website  |
| NMI   | Investing.com | Scrape website  |
| Building Permits   | sdw-wsrest.ecb.europa.eu | Access via RESTful API |
| PPI   | sdw-wsrest.ecb.europa.eu | Access via RESTful API  |
| PPI   | sdw-wsrest.ecb.europa.eu | Access via RESTful API  |
| Debt to GDP Ratio | sdw-wsrest.ecb.europa.eu | Access via RESTful API  |
| Central Bank Balance Sheet (Official reserve assets ) | sdw-wsrest.ecb.europa.eu | Access via RESTful API |

*Follow link for ecb.europa.eu API with Python: https://www.datacareer.de/blog/accessing-ecb-exchange-rate-data-in-python/


## United Kingdom

| Indicator | Source | Comment |
| :---         |     :---:      |          ---: |
| PMI   | Investing.com     | Scrape website  |
| NMI   | Investing.com     | Scrape website  |
| Consumer Confidence   | Investing.com     | Scrape website  |
| Building Permits   | Investing.com     | .xlsx File  |
| CB of England   | Quand     | Create separate chart with visualisation for Balance Sheet  |
| BOP   | ons.gov.uk     | Create separate chart for specific CSV  |

## Canada

| Indicator | Source | Comment |
| :---         |     :---:      |          ---: |
| PMI   | Investing.com | Scrape website  |
| CSI   | Investing.com | Scrape website  |
| Bank Balance Sheet   | .bankofcanada.ca | .csv file with different format |
| PPI   | sdw-wsrest.ecb.europa.eu | Access via RESTful API  |
| BOP   | statcan.gc.ca | .zip file to .xls to format  |

## China

| Indicator | Source | Comment |
| :---         |     :---:      |          ---: |
| PMI   | Investing.com | Scrape website  |
| NMI   | Investing.com | Scrape website  |
| BOP   | api.db.nomics     | Create separate chart for specific CSV  |
| Stock Market Index   | Investing.com | Scrape website  |

## Japan

| Indicator | Source | Comment |
| :---         |     :---:      |          ---: |
| PMI   | Investing.com | Scrape website  |
| CSI   | esri.cao.go.jp | .xlsx file  |
| BOP   | mof.go.jp     | Create separate chart for specific CSV |

## New Zealand

| Indicator | Source | Comment |
| :---         |     :---:      |          ---: |
| PMI   | businessnz.org | .xls file  |
| PSI Services   | businessnz.org | .xls file  |
| M2 Money Supply   | rbnz.govt.nz     | .xlsx file |
| Central Bank Balance Sheet   | rbnz.govt.nz     | .xlsx file |

## Norway

| Indicator | Source | Comment |
| :---         |     :---:      |          ---: |
| PMI   | Investing.com | Scrape website  |
| Building Permits   | sdw.ecb.europa.eu | .xls file  |
| COT Report | Missing | Google Sheet id: 144GCj8WXvzM0H7xSmyWhE5KbtLPpj0wY5vJdEzyTK2o |
| Stock Market Index   | Investing.com | Scrape website  |

## Sweden

| Indicator | Source | Comment |
| :---         |     :---:      |          ---: |
| PMI   | Investing.com | Scrape website  |
| PMI Services  | Investing.com | Scrape website  |
| Building Permits   | sdw.ecb.europa.eu | .xls file  |
| M2 Money Supply   | api.scb.se     | RESTful API Body request |
| Central Bank Balace Sheet   | api.scb.se     | RESTful API Body request |
| BOP   | api.scb.se     | RESTful API Body request |

## Russia

| Indicator | Source | Comment |
| :---         |     :---:      |          ---: |
| PMI   | Investing.com | Scrape website  |
| PMI Services  | Investing.com | Scrape website  |
| BOP   | api.db.nomics     | Create separate chart for specific CSV |
| Central Bank Balace Sheet   | cbr.ru     | .xlsx file |
| Stock Market Index   | iss.moex.com | csv file to format  |

## South Africa

| Indicator | Source | Comment |
| :---         |     :---:      |          ---: |
| PMI   | Investing.com | Scrape website  |
| Employment  | statssa.gov | .xlsx file  |
| Central Bank Balace Sheet   | resbank.co.za     | .csv file to format |
| BOP   | api.db.nomics     | Create separate chart for specific CSV |
| Stock Market Index   | Investing.com | Scrape website  |

## Switzerland

| Indicator | Source | Comment |
| :---         |     :---:      |          ---: |
| PMI   | Investing.com | Scrape website  |
