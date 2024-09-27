from operator import contains
from unittest import skip
import pandas as pd
import numpy as np
import pytest


def test_agg_financials():
    with open('aggregation_pickle1.pkl', 'rb') as pickle_file:
        df_group = pd.read_pickle(pickle_file)
    high_list = df_group['high'].tolist()
    low_list = df_group['low'].tolist()
    close_list = df_group['close'].tolist()   
    import aggregations_ex1
    return_df = aggregations_ex1.agg_financials()
    assert return_df.shape == (6,4)
    return_high_list = return_df['high'].tolist()
    return_low_list = return_df['low'].tolist()
    return_close_list = return_df['close'].tolist()
    assert high_list == return_high_list
    assert low_list == return_low_list
    assert close_list == return_close_list


# Delete the following line to test your next function
@pytest.mark.skip
def test_summary_financials():
    with open('aggregation_pickle2.pkl', 'rb') as pickle_file:
        df_group = pd.read_pickle(pickle_file)
    high_mean_list = df_group['high']['mean'].tolist()
    low_amin_list = df_group['low']['amin'].tolist()   
    import aggregations_ex2
    return_df = aggregations_ex2.summary_financials()
    assert return_df.shape == (6,10)
    return_high_mean_list = return_df['high']['mean'].tolist()
    return_low_amin_list = return_df['low']['amin'].tolist()
    assert high_mean_list == return_high_mean_list
    assert low_amin_list == return_low_amin_list
