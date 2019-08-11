import numpy as np
from strategy import vix_list
from strategy import vx
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
from datetime import datetime
import statsmodels.api as stat
print(vx.head())
x = vix_list[0]
y = vix_list[1]
z = vix_list[2]


#vix_list[0] is spot, [1] is VX1, [2] is VX2

# Add set of axes to figure

def historical_spread():
    fig = plt.figure(figsize=(10, 12),)
    plt.style.use('seaborn')
    # [left, bottom, width, height]
    # main axes
    axes2 = fig.add_axes([0.05, 0.1, 0.9, 0.8])
    # ax = fig.add_axes([0,0,1,1])
    # Plot on that set of axes


    axes2.plot(x - y, marker='', ls='--', color='r', label = 'VIX-VX1')
    axes2.plot(y - z, marker='', color='blue', label = 'VIX-VX2')
    axes2.plot(x - z, marker='', ls=':', color='green', label = 'VX1-VX2')
    axes2.plot(x-vix_list[3], marker = '', ls = '-', color = 'orange', label = 'VIX-VX3')
    axes2.plot(x - vix_list[4], marker = '.', ls = 'dashdot', color = 'gray', label = 'VIX - VX4')
    majoryticks = list(np.linspace(-5.0,10.0,100))
    #axes2.set_yticks(ticks= majoryticks, minor=True)
    axes2.set_title('VIX SPREADS')
    #majorxticks = list(datetime.)
    axes2.legend(loc = 0)
    plt.show()

def spread_regression_plot():
    fig = plt.figure(figsize=(8,8))
    plt.style.use('seaborn')
    axes1 = fig.add_axes([0.05, 0.1, 0.8, 0.8])
    axes1.plot(x, y, marker='o', ls='', color='g', markersize=5, label = 'SPOT/VX1')
    axes1.plot(x, z, marker='o', ls='', color='r', markersize=5, label = 'SPOT/VX2')
    axes1.plot(y, z, marker='o', ls='', color='orange', markersize=5, alpha=0.4, label = 'VX1/VX2')
    axes1.plot(x , vix_list[3], marker = '*',ls = '', color = 'y', markersize = 5, label = 'VIX/VX3')
    axes1.plot(x,vix_list[4], marker = '.', ls = '', color = 'black', markersize = 5 , label = 'VIX/VX4')
    axes1.legend(loc = 0)
    plt.show()


def histogram():
    fig = plt.figure(figsize=(12,12))
    axes1 = fig.add_axes([0.05, 0.1,0.8,0.8])
    axes1.hist(vx['Adj Close'], bins = 'auto')
    plt.show()