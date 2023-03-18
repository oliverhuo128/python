from unittest import skip
import pandas as pd
import numpy as np
import pytest


# Creating the 3 DataFrames, required for the Exercise
data1 = {'Name': ['Mike', 'Saly', 'Randall', 'Boo'],
          'Strength': [1,99,35,5],
          'Speed':[3,65,99,5],
          'Type':['Monster', 'Monster', 'EvilMonster', 'Human']}
df1 = pd.DataFrame(data1)


data2 = {'Name': ['Fungus', 'Celia', 'Waternoose'],
        'Strength': [np.nan, 40,51],
        'Speed':[3, np.nan, 35],
        'Type':['Monster', 'Monster', 'EvilMonster'],
        'Color':['Orange', 'Purple', 'Gray'],
        'MCODE':[223423, 223422, 223234]}
df2 = pd.DataFrame(data2, index = [90,91,92])


data3 = {'Species':['Monster', 'Human', 'EvilMonster', 'Donut'],
          'FavouriteFood':['Screams', 'Candy', np.nan, 'Flour']}
df3 = pd.DataFrame(data3)





def test_combine_monster():
    import combining_sorting_ex1
    new_df = combining_sorting_ex1.combine_monster(df1,df2,df3)
    assert new_df.shape == (7,6)
    mask = new_df['Type'] == 'EvilMonster'
    evilmonster_food = new_df[mask]['FavouriteFood'].tolist()
    assert evilmonster_food[0] == 'ExtremeScreams'
    assert new_df['Strength'].sum() == 269.5
    assert new_df['Speed'].sum() == 245
