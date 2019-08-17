from backtest import cointegration_test
from portfolio_and_default_data import macro_data
from portfolio_and_default_data import portfolio
from keys_settings import date
from portfolio_and_default_data import currency_data
from forex_python.converter import CurrencyRates
import pull_historical_data as pull
import keys_settings as ks
symbol = pull.pull_symbol(ks.symbol, ks.source)
symbol.reset_index(inplace= True)
#work to make it so that adj close is uniform between download sources
symbol = pull.compute_price_data(symbol, symbol['Adj Close'])#may switch to "Settle for quandl
symbol.set_index(symbol['Date'], inplace = True)

aud_jpy = ['AUD/JPY']
vix = ['^VIX']
#vix['Symbol'] = 'VIX'
vx1 = ['VX1']
vx2 = ['VX2']
vx3 = ['VX3']
vx4 = ['VX4']

aud_jpy = currency_data.loc[currency_data['Symbol'].isin(aud_jpy)]
aud_jpy.set_index('Date', inplace = True)
vix = portfolio.loc[portfolio['Symbol'].isin(vix)]
vx1 = macro_data.loc[macro_data['Symbol'].isin(vx1)]
vx2 = macro_data.loc[macro_data['Symbol'].isin(vx2)]
vx3 = macro_data.loc[macro_data['Symbol'].isin(vx3)]
vx4 = macro_data.loc[macro_data['Symbol'].isin(vx4)]
vix.set_index(vix['Date'], inplace = True)
vx1.set_index(vx1['Date'], inplace = True)
vx2.set_index(vx2['Date'], inplace = True)
vx3.set_index(vx2['Date'], inplace = True)
vx4.set_index(vx2['Date'], inplace = True)


vx1_vx2_vx4_vx4 = [vx1[['Date', 'Symbol','Settle']], vx2[['Date','Symbol','Settle']],vx3[['Date','Symbol','Settle']],vx4[['Date','Symbol','Settle']]]
vx = vx1[['Settle']].join(vx2[['Settle']], on = 'Date', lsuffix = '_vx1', rsuffix = '_vx2')
vx = vx.join(vx3[['Settle']])
vx = vx.join(vx4[['Settle']], rsuffix = '_vx4')
vx = vx.join(vix[['Adj Close']])
vx.drop_duplicates(inplace= True)
vx.dropna(inplace = True)
vx['VIX-VX1 Spread'] = (vx['Adj Close'] - vx['Settle_vx1'])
vx['VX1-VX2 Spread'] = (vx['Settle_vx1'] - vx['Settle_vx2'])
vx['VIX-VX2 Spread'] = (vx['Adj Close'] - vx['Settle_vx2'])
vx['VIX-VX3 Spread'] = (vx['Adj Close'] - vx['Settle'])
vx['VIX-VX4 Spread'] = (vx['Adj Close'] - vx['Settle_vx4'])
vix_list = [vx['Adj Close'], vx['Settle_vx1'],vx['Settle_vx2'],vx['Settle'],vx['Settle_vx4']]
print('AUD/JPY SPOT:')
print(aud_jpy['Value'].loc[date])
print('The VIX SPOT PRICE: ')
print(vx['Adj Close'].loc[date])
print('The VIX 1M PRICE: ')
print(vx['Settle_vx1'].loc[date])
print('The VIX 2M PRICE: ')
print(vx['Settle_vx2'].loc[date])
print('The VIX 3M PRICE: ')
print(vx['Settle'].loc[date])
print('The VIX 4M PRICE: ')
print(vx['Settle_vx4'].loc[date])
x = vix_list[0]
y = vix_list[1]
print('VIX over VX1:')
print(cointegration_test( x , y))
x = vix_list[0]
y = vix_list[2]
print('VIX over VX2:')
print(cointegration_test(x,y))
x = vix_list[1]
y = vix_list[2]
print('VX1 over VX2:')
print(cointegration_test(x,y))


print(symbol['30 Day Vol'].tail())