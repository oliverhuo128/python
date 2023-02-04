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



def test_loc_monster():
    import selection_ex1
    loc_values = selection_ex1.loc_monster(df)
    assert loc_values['fungus_speed'] == 3
    assert loc_values['celias_type'] == 'Monster'
    assert loc_values['waternoose_mcode'] == 223234


# Delete the following line to test your next function
@pytest.mark.skip
def test_iloc_monster():
    import selection_ex2
    iloc_values = selection_ex2.iloc_monster(df)
    assert iloc_values['fungus_speed'] == 3
    assert iloc_values['celias_type'] == 'Monster'
    assert iloc_values['waternoose_mcode'] == 223234


# Delete the following line to test your next function
@pytest.mark.skip
def test_loc_slice_monster():
    import selection_ex3
    new_df = selection_ex3.loc_slice_monster(df)
    assert new_df.shape == (2,5)
    assert new_df.loc[90,'Name'] == 'Fungus'
    assert new_df.loc[91, 'Color'] == 'Purple'


# Delete the following line to test your next function
@pytest.mark.skip
def test_iloc_slice_monster():
    import selection_ex4
    new_df = selection_ex4.iloc_slice_monster(df)
    assert new_df.shape == (2,5)
    assert new_df.iloc[0,0] == 40
    assert new_df.iloc[1,4] == 223234


# Delete the following line to test your next function
@pytest.mark.skip
def test_bool_mask_monster():
    import selection_ex5
    new_df = selection_ex5.bool_mask_monster(df)
    assert new_df.shape == (2,6)
    assert 'EvilMonster' not in new_df['Type']

