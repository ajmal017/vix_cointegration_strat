import numpy as np
import keys_settings as ks
from strategy import vix_list
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
from pull_historical_data import pull_symbol
from pull_historical_data import compute_price_data
from keys_settings import symbol
from datetime import datetime
import statsmodels.api as stat
print(vx.head())
vix = vix_list[0]
vx1 = vix_list[1]
vx2 = vix_list[2]


symbol.reset_index(inplace= True)
compute_price_data(symbol, symbol['Adj Close'])
symbol.set_index(symbol['Date'], inplace=True)

#vix_list[0] is spot, [1] is VX1, [2] is VX2

# Add set of axes to figure

def historical_spread():
    fig = plt.figure(figsize=(10, 12),)
    plt.style.use('seaborn dark')
    # [left, bottom, width, height]
    # main axes
    axes2 = fig.add_axes([0.05, 0.1, 0.9, 0.8])
    # ax = fig.add_axes([0,0,1,1])
    # Plot on that set of axes


    axes2.plot( vix - vx1, marker='', ls='--', color='r', label = 'VIX-VX1')
    axes2.plot(vx1 - vx2, marker='', color='blue', label = 'VIX-VX2')
    axes2.plot(vix - vx2, marker='', ls=':', color='green', label = 'VX1-VX2')
    axes2.plot(vix-vix_list[3], marker = '', ls = '-', color = 'orange', label = 'VIX-VX3')
    axes2.plot(vix - vix_list[4], marker = '.', ls = 'dashdot', color = 'gray', label = 'VIX - VX4')
    majoryticks = list(np.linspace(-5.0,10.0,100))
    #axes2.set_yticks(ticks= majoryticks, minor=True)
    axes2.set_title('VIX SPREADS')
    #majorxticks = list(datetime.)
    axes2.legend(loc = 0)
    plt.show()

def spread_regression_plot():
    fig = plt.figure(figsize=(8,8))
    plt.style.use('seaborn dark')
    axes1 = fig.add_axes([0.05, 0.1, 0.8, 0.8])
    axes1.plot(vix, vx1, marker='o', ls='', color='g', markersize=5, label = 'SPOT/VX1')
    axes1.plot(vix, vx2, marker='o', ls='', color='r', markersize=5, label = 'SPOT/VX2')
    axes1.plot(vx1, vx2, marker='o', ls='', color='orange', markersize=5, alpha=0.4, label = 'VX1/VX2')
    axes1.plot(vix , vix_list[3], marker = '*',ls = '', color = 'y', markersize = 5, label = 'VIX/VX3')
    axes1.plot(vix,vix_list[4], marker = '.', ls = '', color = 'black', markersize = 5 , label = 'VIX/VX4')
    axes1.legend(loc = 0)
    plt.show()


def histogram():
    fig = plt.figure(figsize=(12,12))
    plt.style.use('ggplot')
    axes1 = fig.add_axes([0.05, 0.1,0.8,0.8])
    axes1.hist(vx['Adj Close'], bins = 60, color = 'green')
    plt.show()

def vol_clustering():
    fig = plt.figure()
    plt.style.use('fivethirtyeight')
    # [left, bottom, width, height]
    axes1 = fig.add_axes([0.72, 0.72, 0.16, 0.16])
    #axes2 = fig.add_axes([0.72, 0.72, 0.16, 0.16])
    #axes3 = fig.add_axes([0.72, 0.72, 0.16, 0.16])
    axes1.plot(vx['VIX-VX1 30 Day Mean'])
    #axes2.plot(vx['VIX-VX1 30 Day STD'], color = 'red')
    #axes3.plot(symbol['Returns'], color = 'blue', marker = '')
    plt.show()

def hull_moving_avg_plot():
    fig = plt.figure(figsize=(8,8))
    plt.style.use('seaborn')
    axes1 = fig.add_axes([0.05, 0.1, 0.8, 0.8])
    axes1.plot(symbol['Adj Close'], marker='o', ls='--', color='g', markersize=5, label = 'Close')
    axes1.plot(symbol['hull_moving_avg'], marker = '',color = 'red', markersize=5, label = 'Hull MA')
    axes1.legend(loc = 0)

    plt.plot(symbol['hull_moving_avg'])
    plt.show()
'''While it is possible to adjust the spacing between the subplots using subplots_adjust, or use the 
gridspec functionality for more advanced subplotting, it is often easier to just use the more general 
add_axes method instead of add_subplot. The add_axes method takes a list of four values, which are xmin,
 ymin, dx, and dy for the subplot, where xmin and ymin are the coordinates of the lower left corner of the 
 subplot, and dx and dy are the width and height of the subplot, with all values specified in relative units 
 (where 0 is left/bottom and 1 is top/right).'''