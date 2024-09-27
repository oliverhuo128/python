from unittest import skip
import pandas as pd
import numpy as np
import pytest



def test_fb_upsample():
    with open('timeseries_pickle1.pkl', 'rb') as pickle_file:
        df_melt = pd.read_pickle(pickle_file)
    date_list = df_melt['formatted_date'].tolist()
    price_type_list = df_melt['price_type'].tolist()
    avg_price_list = df_melt['avg_price'].tolist()
    import timeseries_ex1
    return_df = timeseries_ex1.fb_upsample()
    assert return_df.shape == (9,3)
    return_date_list = return_df['formatted_date'].tolist()
    return_price_type_list = return_df['price_type'].tolist()
    return_avg_price_list = return_df['avg_price'].tolist()
    assert return_date_list == date_list
    assert return_price_type_list == price_type_list
    assert return_avg_price_list == avg_price_list
      

# Delete the following line to test your next function
@pytest.mark.skip
def test_fb_downsample():
    with open('timeseries_pickle2.pkl', 'rb') as pickle_file:
        combined_df = pd.read_pickle(pickle_file)
    date_list = combined_df['formatted_date'].tolist()
    perc_dev_list = combined_df['perc_dev'].tolist()
    import timeseries_ex2
    return_df = timeseries_ex2.fb_downsample()
    assert return_df.shape == (64,4)
    return_date_list = return_df['formatted_date'].tolist()
    return_perc_dev_list = return_df['perc_dev'].tolist()
    assert date_list == return_date_list
    assert perc_dev_list == return_perc_dev_list



 # Delete the following line to test your next function 
@pytest.mark.skip
def test_fb_rolling_stats():
    with open('timeseries_pickle3.pkl', 'rb') as pickle_file:
        new_df = pd.read_pickle(pickle_file)
    date_list = new_df['formatted_date'].tolist()
    diff_list = new_df['first_diff'].tolist()
    import timeseries_ex3
    return_df = timeseries_ex3.fb_rolling_stats()
    assert return_df.shape == (5,4)
    return_date_list = return_df['formatted_date'].tolist()
    return_diff_list = return_df['first_diff'].tolist()
    assert date_list == return_date_list
    assert return_diff_list == diff_list