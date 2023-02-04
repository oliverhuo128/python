import numpy as np
import pandas as pd


# Delete the following code and write your solution:
def fb_downsample():
    from yahoofinancials import YahooFinancials
    data1 = YahooFinancials('FB').get_historical_price_data('2021-10-01', '2022-01-02', 'monthly')
    data2 = YahooFinancials('FB').get_historical_price_data('2021-10-01', '2022-01-02', 'daily')
    data1 = data1['FB']['prices']
    data2 = data2['FB']['prices']
    monthly_prices = pd.DataFrame(data1)[['formatted_date', 'close']]
    daily_prices = pd.DataFrame(data2)[['formatted_date', 'close']]
    monthly_prices['formatted_date'] = pd.to_datetime(monthly_prices['formatted_date'], format = '%Y-%m-%d')
    daily_prices['formatted_date'] = pd.to_datetime(daily_prices['formatted_date'], format = '%Y-%m-%d')
    monthly_prices.set_index('formatted_date', inplace = True)
    monthly_prices = monthly_prices.resample('D').mean()
    monthly_prices.interpolate(inplace = True)
    monthly_prices.reset_index(inplace = True)
    combined_df = pd.merge(daily_prices, monthly_prices, on = 'formatted_date', how = 'left')
    combined_df.rename(columns = {'close_x':'real_close', 'close_y':'inter_close'}, inplace = True)
    combined_df['perc_dev'] = combined_df.apply(lambda row: ((row['inter_close'] - row['real_close'])/row['real_close'])*100, axis = 1)
    return combined_df