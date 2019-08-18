import os as os
import datetime as datetime
from pull_historical_data import pull_symbol
api_key = 'B6KP8sRUDocDsQw1zc8n'
alphavantage_api_key = '9VORVZNAJ67273RW'
start = '2017-12-15'
today = datetime.date.today()
end = '2019-08-07'
initial_capital = 1000000
symbol = 'SPY'
symbol = symbol.upper()
source = 'yahoo finance'
source = source.lower()
sma = 20
lma = 50

#Specify a date
date = '2018-02-05'

symbol = pull_symbol(symbol,source)

#Save Paths
os.getcwd()
dataset_write_path = r"C:/Users/Faye Brugman/PycharmProjects/vix_cointegration_strat/dataset.csv"
portfolio_write_path = r"C:/Users/Faye Brugman/PycharmProjects/vix_cointegration_strat/portfolio.csv"
sql_dataset = r"C:/Users/Faye Brugman/PycharmProjects/vix_cointegration_strat/dataset.sql"
sql_portfolio = r"C:/Users/Faye Brugman/PycharmProjects/vix_cointegration_strat/portfolio.sql"
investment_list = ['SPY','TLT','IEF','GLD','DBC', 'SSO','QLD','QQQ', 'XLV','XLU','IWM', 'DIA', 'EEM', '^VIX']
dataset_list = ['SP500','Gold', 'VX1','VX2', 'VX3','VX4']
currency_write_path = r"C:/Users/Faye Brugman/PycharmProjects/vix_cointegration_strat/currency.csv"

urls = ['CHRIS/CME_ES1', 'CHRIS/CME_GC1', 'CHRIS/CBOE_VX1', 'CHRIS/CBOE_VX2', 'CHRIS/CBOE_VX3', 'CHRIS/CBOE_VX4', ]
currency_list = ['AUD/JPY']
currency_urls = ['RBA/FXRJY']
#'CHRIS/CME_ZC1','CHRIS/CME_ZS1']'WTI Crude','Brent Crude','Dollar',]
#'CHRIS/CME_CL1', 'CHRIS/CME_BB1', 'CHRIS/ICE_DX1',