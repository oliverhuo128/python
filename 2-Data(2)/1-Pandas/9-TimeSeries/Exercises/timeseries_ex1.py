import numpy as np
import pandas as pd


# Delete the following code and write your solution:
def fb_upsample():
    from yahoofinancials import YahooFinancials
    data = YahooFinancials('FB').get_historical_price_data('2019-01-01', '2022-01-01', 'monthly')
    data = data['FB']['prices']
    df = pd.DataFrame(data)
    df = df[['formatted_date', 'high', 'low', 'close']]
    df['formatted_date'] = pd.to_datetime(df['formatted_date'], format = '%Y-%m-%d')
    df.set_index('formatted_date', inplace = True)
    df_upsample = df.resample('Y').mean()
    df_upsample.reset_index(inplace = True)
    df_melt = df_upsample.melt(id_vars = ['formatted_date'], var_name = 'price_type', value_name = 'avg_price')
    df_melt.sort_values(['formatted_date', 'price_type'], ascending = [True, True], inplace = True)
    return df_melt