import numpy as np
import pandas as pd
from pull_historical_data import portfolio
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()
DataFrame = pd.DataFrame

symbol = ['SPY']
symbol = portfolio.loc[portfolio['Symbol'].isin(symbol)]
symbol = DataFrame(symbol)
symbol.set_index(symbol['Date'], inplace = True)
#define the period
period = 13
#symbol['WMA'] = symbol['Adj Close'].ewm(span = period, adjust = True)
symbol['WMA'] = symbol['Adj Close'].rolling(period).mean()
#First weight is range 1 to period in -1 increments
weights = list(range(0,period, 1))
#set price as the last n periods
#divide the period by 2
period2 = int(period/2)
period3 = int(np.sqrt(period))

#symbol['WMA'] = symbol['Adj Close'].iloc[(-1*period),0].ewm(span=period,adjust=False).mean()
symbol['WMA2'] = symbol['Adj Close'].rolling(period2).mean()
#symbol['WMA'] = symbol['Adj Close'].iloc[:,0].ewm(span=40,adjust=False).mean()
symbol['WMA_2_x_2'] = symbol['WMA2']*2
symbol['WMA3'] = symbol['WMA_2_x_2'] - symbol['WMA']
symbol['hull_moving_avg'] = symbol['WMA3'].rolling(period3).mean()
#Sqrt(Period)WMA[WMA3]
#Sqrt(Period)WMA[2 x (Period/2) WMA(Price) - Period WMA(Price)]

#weights = list(range(0,period2,1))

#WMA2 = WMA2*2
#create a third MA that is the difference of 1 and 2
#WMA3 = WMA2 - WMA1
#take the square root of the period
#weights = list(range(1,period3,1))




print(type(symbol))
print(symbol[['WMA','WMA2','WMA3','hull_moving_avg']].tail())

##plot the figure
fig = plt.figure(figsize=(8,8))
plt.style.use('seaborn')
axes1 = fig.add_axes([0.05, 0.1, 0.8, 0.8])
axes1.plot(symbol['Adj Close'], marker='o', ls='', color='g', markersize=5, label = 'Close')
axes1.plot(symbol['hull_moving_avg'], marker='', color='r', markersize=5, label = 'Hull MA')
axes1.legend(loc = 0)

plt.plot(symbol['hull_moving_avg'])
plt.show()
"""
potential maths to consider


granger causality
statsmodels.stattools.grangercausalitytests

"We say that a variable X that evolves over time Granger-causes another evolving
variable Y if predictions of the value
of Y based on its own past values and on the past values of X are better than
predictions of Y based only on its own past values."
Two Assumptions
1. The cause happens prior to its effect
2. The cause has unique information about the future values of its effect
3. Used on time series




"""