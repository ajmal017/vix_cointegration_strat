import numpy as np
import pandas as pd
import quandl
import keys_settings as ks
import yfinance as yf
from pandas import DataFrame
from sqlalchemy import create_engine
#engine = create_engine('sqlite:///database.db')

#get yfinance data from VIX
#aud_jpy_spot = ForeignExchange.get_currency_exchange_daily()
#cc = ForeignExchange(key=ks.alphavantage_api_key, output_format= 'pandas')
#curr_data, meta_data = cc.get_currency_exchange_daily(from_symbol= 'AUD', to_symbol= 'JPY', outputsize= 'full')

#Create an investment list and download from yfinance
def pull_symbol(symbol, source):
    data = []
    if source == 'yahoo finance':
    #set to today. Can change the end date
        data = yf.download(tickers = symbol, start = ks.start, end = ks.today)
        data['Symbol'] = symbol
        data.to_csv(symbol + '.txt')
    elif source == 'quandl':
        print('Enter Symbol Name:')
        data = quandl.get(dataset=symbol, start_date = ks.start,end_date = ks.today, api_key = ks.api_key)
        data['Symbol'] = input()
    else:
        data = print('Its not here yet dude . . .')
    return data

#after pulling data from quandl or yfinance, you can compute standard price data listed below
#you gotta reset the index of the DataFrame unfortunately.
def compute_price_data(Dataset, Price_input):
    Dataset['Prev_Close'] = Dataset.groupby(Dataset['Symbol'])['Adj Close'].shift(1)
    Dataset['Returns'] = (np.log(Price_input / Dataset['Prev_Close']))
    Dataset['Year'] = pd.DatetimeIndex(Dataset['Date']).year
    Dataset['Prev_Close_Yrly'] = Dataset.groupby(['Symbol', 'Year'])['Adj Close'].shift(1)
    Dataset['quarter'] = pd.DatetimeIndex(Dataset['Date']).quarter
    Dataset['Previous_close_qrtr'] = Dataset.groupby(['Symbol', 'Year', 'quarter'])['Adj Close'].shift(1)
    Dataset['cum_returns'] = Dataset.groupby(['Symbol']).cumsum()['Returns']
    Dataset['Yrly_Returns'] = np.log(Price_input / Dataset['Prev_Close_Yrly'])
    Dataset['Qrtrly_Returns'] = np.log(Price_input / Dataset['Previous_close_qrtr'])
    Dataset['30 Day Vol'] = Price_input.rolling(30).std()
    Dataset.dropna(inplace=True)
    return Dataset