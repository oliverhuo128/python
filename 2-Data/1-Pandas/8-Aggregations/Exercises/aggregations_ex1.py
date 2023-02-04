import numpy as np
import pandas as pd


# Delete the following code and write your solution:
def agg_financials():
    from yahoofinancials import YahooFinancials
    data = YahooFinancials('AAPL').get_historical_price_data('2021-07-01', '2022-01-01', 'daily')
    df = data['AAPL']['prices']
    df = pd.DataFrame(df)
    df = df[['formatted_date', 'high', 'low', 'close']]
    df['formatted_date'] = pd.to_datetime(df['formatted_date'], format = '%Y-%m-%d')
    df['Month'] = df['formatted_date'].dt.to_period('M')
    df_group = df.groupby('Month').agg({'high':np.max, 'low':np.min, 'close':np.mean})
    df_group.reset_index(inplace = True)
    return df_group