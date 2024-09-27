from unittest import skip
import pandas as pd
import numpy as np
import pytest


# Creating the DataFrame, required for the Exercises
data = {'Name': ['Fungus', 'Celia', 'Waternoose'],
        'Strength': [np.nan, 40,51],
        'Speed':[3, np.nan, 35],
        'Type':['Monster', 'Monster', 'EvilMonster'],
        'Color':['Orange', 'Purple', 'Gray'],
        'MCODE':[223423, 223422, 223234]}
df = pd.DataFrame(data, index = [90,91,92])




def test_interpolate_monster():
    import missing_data_ex1
    new_df = missing_data_ex1.interpolate_monster(df)
    assert new_df.shape == (2, 6)
    assert new_df.loc[91, "Speed"] == 19


# Delete the following line to test your next function
@pytest.mark.skip
def test_impute_monster():
    import missing_data_ex2
    new_df = missing_data_ex2.impute_monster(df)
    assert new_df.loc[91, "Speed"] == 19
    assert new_df.loc[90, 'Strength'] == 40



