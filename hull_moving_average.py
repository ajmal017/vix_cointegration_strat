import numpy as np
import pandas as pd
from keys_settings import symbol
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
from backtest import linear_weight_moving_average
register_matplotlib_converters()
DataFrame = pd.DataFrame

symbol = DataFrame(symbol)
symbol.reset_index(inplace= True)
#define the period
period = 13
close = symbol['Adj Close'].to_numpy()
symbol['WMA'] = linear_weight_moving_average(close, period)
#divide the period by 2
period2 = int(period/2)
symbol['WMA2'] = linear_weight_moving_average(close, period2)
symbol['WMA_2_x_2'] = symbol['WMA2']*2
symbol['WMA3'] = symbol['WMA_2_x_2'] - symbol['WMA']
period3 = int(np.sqrt(period))
WMA3 = symbol['WMA3'].to_numpy()
symbol['hull_moving_avg'] = linear_weight_moving_average(WMA3, period3)
symbol.set_index(symbol['Date'], inplace = True)
#Sqrt(Period)WMA[WMA3]
#Sqrt(Period)WMA[2 x (Period/2) WMA(Price) - Period WMA(Price)]
#WMA2 = WMA2*2
#create a third MA that is the difference of 1 and 2
#WMA3 = WMA2 - WMA1
#take the square root of the period
#weights = list(range(1,period3,1))





print(symbol[['Adj Close','WMA','WMA2','WMA_2_x_2','WMA3','hull_moving_avg']].tail())
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