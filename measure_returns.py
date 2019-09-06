from portfolio_and_default_data import portfolio
print(portfolio[['Symbol','Returns']].groupby('Symbol').sum())
print(portfolio[['Year','Symbol', 'Yrly_Returns']])
