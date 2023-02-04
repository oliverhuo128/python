import numpy as np
import pandas as pd


# Delete the following code and weite your solution:
def fb_rolling_stats():
    from yahoofinancials import YahooFinancials
    data = YahooFinancials('FB').get_historical_price_data('2021-12-01', '2022-01-01', 'daily')
    data = data['FB']['prices']
    df = pd.DataFrame(data)
    df = df[['formatted_date', 'close']]
    df['formatted_date'] = pd.to_datetime(df['formatted_date'], format = '%Y-%m-%d')
    df.set_index('formatted_date', inplace = True)
    df['perc_change'] = df['close'].pct_change()
    df['first_diff'] = df['close'].diff(1)
    mask = df['perc_change'] >0.02
    new_df = df[mask]
    new_df.reset_index(inplace = True)
    return new_df