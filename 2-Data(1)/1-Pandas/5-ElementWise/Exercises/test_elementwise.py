from unittest import skip
import pandas as pd
import numpy as np
import pytest


# Creating the DataFrame, required for the Exercises
data = {'Name': ['Mike', 'Saly', 'Randall', 'Boo'],
          'Strength': [1,99,35,5],
          'Speed':[3,65,99,5],
          'Type':['Monster', 'Monster', 'EvilMonster', 'Human']}
df = pd.DataFrame(data)



def test_stat_monster():
    import elementwise_ex1
    new_df = elementwise_ex1.stat_monster(df)
    assert new_df.shape == (4, 7)
    avg_stat_list = [2, 82, 67, 5]
    min_stat_list = [1,65,35,5]
    max_stat_list = [3,99,99,5]
    new_df_avg = new_df['AvgStat'].tolist()
    new_df_min = new_df['MinStat'].tolist()
    new_df_max = new_df['MaxStat'].tolist()
    assert avg_stat_list == new_df_avg
    assert min_stat_list == new_df_min
    assert max_stat_list == new_df_max


# Delete the following line to test your next function
@pytest.mark.skip
def test_boost_monster():
    import elementwise_ex2
    new_df = elementwise_ex2.boost_monster(df)
    assert new_df.shape == (4, 6)
    boost_speed_list = [6,130,99,5]
    boost_strength_list = [1,99,105, 5]
    new_df_boost_speed = new_df['BoostSpeed'].tolist()
    new_df_boost_strength = new_df['BoostStrength'].tolist()
    assert boost_speed_list == new_df_boost_speed
    assert boost_strength_list == new_df_boost_strength 
