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
investment_list = ks.investment_list
investments = {}
i = 0
for i in investment_list:
    investments[i] = i+'.txt'
li = []
for k, v in investments.items():
    try:
        df = yf.download(k, start= ks.start, end = ks.end)
        df.reset_index(inplace = True)
        df['Symbol'] = k
        li.append(df)
    except ValueError:
        pass
        print('pass on:', k)
portfolio = pd.concat(li, axis = 0, ignore_index= True)
pfolio = portfolio.to_csv(ks.portfolio_write_path)
portfolio['Prev_Close'] = portfolio.groupby(portfolio['Symbol'])['Adj Close'].shift(1)
portfolio['Returns']= (np.log(portfolio['Adj Close']/portfolio['Prev_Close']))
portfolio['Year'] = pd.DatetimeIndex(portfolio['Date']).year
portfolio['Prev_Close_Yrly'] = portfolio.groupby(['Symbol', 'Year'])['Adj Close'].shift(1)
portfolio['quarter'] = pd.DatetimeIndex(portfolio['Date']).quarter
portfolio['Previous_close_qrtr'] = portfolio.groupby(['Symbol', 'Year', 'quarter'])['Adj Close'].shift(1)
portfolio['cum_returns'] = portfolio.groupby(['Symbol']).cumsum()['Returns']
portfolio['Yrly_Returns'] = np.log(portfolio['Adj Close']/portfolio['Prev_Close_Yrly'])
portfolio['Qrtrly_Returns'] = np.log(portfolio['Adj Close']/portfolio['Previous_close_qrtr'])
portfolio['30 Day Vol'] = portfolio['Adj Close'].rolling(30).std()
portfolio.dropna(inplace = True)
#pfolio = portfolio.to_sql(ks.sql_portfolio, con = engine)
# get quandl data for dictionary and concat to a dataframe using the dictionaries, urls, from keys_settings
data = dict(zip(ks.dataset_list, ks.urls))
li = []
for k, v in data.items():
    try:
        df = quandl.get(dataset=v, start_date=ks.start, end_date=ks.end, api_key=ks.api_key)
        df.reset_index(inplace=True)
        df['Symbol'] = k
        df.columns.values[0] = 'Date'
        li.append(df)
    except ValueError:
        print('pass on:', k)
macro_data = pd.concat(li, axis=0, ignore_index=True, sort=True)
macro_data.drop(labels= ['Close', 'Total Volume', 'Volume', 'Prev. Day Open Interest', 'Last', 'Previous Day Open Interest', 'EFP'], axis = 1, inplace= True)
#macro_data.columns.values[6] = 'Volume'
#macro_data.drop(labels=['Change', 'Block Volume', 'EFP Volume', 'EFS Volume', 'Wave'], axis=1, inplace=True)
macro_data['Previous Settle'] = macro_data.groupby(macro_data['Symbol'])['Settle'].shift(1)
macro_data['Net-Change'] = macro_data['Settle'] - macro_data['Previous Settle']
macro_data['Percent Change'] = (macro_data['Net-Change']/macro_data['Previous Settle'])*100
macro_data['Cumulative Change'] = macro_data.groupby(macro_data['Symbol']).cumsum()['Net-Change']
macro_data['Log Returns'] = (np.log(macro_data['Settle']/macro_data['Previous Settle']))
macro_data['Cumulative Log Change'] = macro_data['Log Returns'].cumsum()
macro_data['30 Day Vol'] = macro_data['Settle'].rolling(30).std()
macro_csv = macro_data.to_csv(ks.dataset_write_path)
#portfolio['Returns']= (np.log(portfolio['Adj Close']/portfolio['Prev_Close']))
#macro_sql = macro_data.to_sql(ks.sql_dataset, con = engine )

data = dict(zip(ks.currency_list, ks.currency_urls))
li = []
for k, v in data.items():
    try:
        df = quandl.get(dataset=v, start_date=ks.start, end_date=ks.end, api_key=ks.api_key)
        df.reset_index(inplace=True)
        df['Symbol'] = k
        df.columns.values[0] = 'Date'
        li.append(df)
    except ValueError:
        print('pass on:', k)
currency_data = pd.concat(li, axis=0, ignore_index=True, sort=True)
currency_data['Previous_Value'] = currency_data.groupby(currency_data['Symbol'])['Value'].shift(1)
currency_data['Net-Change'] = currency_data['Value'] - currency_data['Previous_Value']
currency_data['Percent Change'] = (currency_data['Net-Change']/currency_data['Previous_Value'])*100
currency_data['Cumulative Change'] = currency_data.groupby(currency_data['Symbol']).cumsum()['Net-Change']
currency_data['Log Returns'] = (np.log(currency_data['Value']/currency_data['Previous_Value']))
currency_data['Cumulative Log Change'] = currency_data['Log Returns'].cumsum()
currency_csv = currency_data.to_csv(ks.currency_write_path)

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

#print(portfolio['Adj Close'].loc[portfolio['Symbol'] == '^VIX'])


