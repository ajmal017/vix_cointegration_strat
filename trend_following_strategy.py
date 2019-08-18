from hull_moving_average import symbol
from keys_settings import initial_capital

symbol['EMA'] = symbol['Adj Close'].ewm(span = 13, adjust = False).mean()
print(symbol[['Adj Close','WMA','EMA']].tail())

#Data['Buy'] = Data.apply(lambda x: x['Close'] if x['SMA']> x['LMA'] and x['SMA2']< x['LMA2'] else 0, axis = 1)
#Data['Sell'] = Data.apply(lambda y: y['Close'] if y['SMA']< y['LMA'] and y['SMA2']> y['LMA2'] else 0, axis = 1)
#calculate a column Named "Strategy"
symbol['BUY'] = symbol.apply(lambda x: -1*(x['Adj Close']) if x['Adj Close'] > x['hull_moving_avg'] else 0, axis = 1)
symbol['SELL'] = symbol.apply(lambda x: x['Adj Close'] if x['Adj Close'] < x['hull_moving_avg'] else 0, axis = 1)
symbol['Strategy'] = 0.35*(initial_capital)*(symbol['BUY']+symbol['SELL']).cumsum()

'''
def hull_moving_average_strat():
    i = 0
    today = symbol['hull_moving_avg']
    yesterday = symbol['hull_moving_avg'].shift(1)
    if today > yesterday:
        symbol['Strategy'] = i + 1
    elif today < yesterday:
        symbol['Strategy'] = i - 1
    else:
        symbol['Strategy'] = i
    return symbol['Strategy']
hull_moving_average_strat()
'''
print(symbol[['BUY','SELL','Strategy']])
