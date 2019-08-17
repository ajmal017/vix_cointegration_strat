import numpy as np
import pandas as pd
import statsmodels
import statsmodels.api as stat
import statsmodels.tsa.stattools as ts
#determine cointegration
def cointegration_test(x,y):
    result = stat.OLS(x,y).fit()
    adf_results = ts.adfuller(result.resid)
    if adf_results[0] <= adf_results[4]['10%']:
        return 'Pair is cointegrated'
    else:
        return 'Pair is not cointegrated'
#linear_weighted_moving_average takes an array and returns a series. Turn Series.to_numpy for variable you're attempting
#to weigh. Note that indexes must line up
def linear_weight_moving_average(signal, period):
    buffer = [np.nan] * period
    for i in range(period, len(signal)):
        buffer.append(
            (signal[i - period : i] * (np.arange(period) + 1)).sum()
            / (np.arange(period) + 1).sum()
        )
    return pd.Series(buffer)

