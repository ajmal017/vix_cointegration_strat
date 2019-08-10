#determine cointegration
import pandas as pd
from pull_historical_data import macro_data
import statsmodels
import statsmodels.api as stat
import statsmodels.tsa.stattools as ts
import matplotlib.pyplot as plt
def cointegration_test(x,y):
    result = stat.OLS(x,y).fit()
    adf_results = ts.adfuller(result.resid)
    if adf_results[0] <= adf_results[4]['10%']:
        return 'Pair is cointegrated'
    else:
        return 'Pair is not cointegrated'


