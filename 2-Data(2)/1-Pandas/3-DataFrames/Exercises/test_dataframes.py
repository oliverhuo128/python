from unittest import skip
import pandas as pd
import pytest


def test_create_monster_lol():
    import dataframes_ex1
    df = dataframes_ex1.create_monster_lol()
    assert df.loc[0, 'Name'] == 'Mike'
    assert df.loc[1,'Strength'] == 99
    assert df.loc[2, 'Speed'] == 99
    assert df.loc[3, 'Type'] == 'Human'
    assert df.shape == (4,4)

# Delete the next following line to test your corresponding function
@pytest.mark.skip
def test_create_monster_lod():
    import dataframes_ex2
    df = dataframes_ex2.create_monster_lol()
    assert df.loc[0, 'Name'] == 'Mike'
    assert df.loc[1,'Strength'] == 99
    assert df.loc[2, 'Speed'] == 99
    assert df.loc[3, 'Type'] == 'Human'
    assert df.shape == (4,4)

# Delete the next following line to test your corresponding function
@pytest.mark.skip
def test_create_monster_dol():
    import dataframes_ex3
    df = dataframes_ex3.create_monster_lol()
    assert df.loc[0, 'Name'] == 'Mike'
    assert df.loc[1,'Strength'] == 99
    assert df.loc[2, 'Speed'] == 99
    assert df.loc[3, 'Type'] == 'Human'
    assert df.shape == (4,4)


# Delete the next following line to test your corresponding function
@pytest.mark.skip
def test_create_reset_monster():
    import dataframes_ex4
    import dataframes_ex2
    df = dataframes_ex4.create_reset_monster(dataframes_ex2.create_monster_lod)
    df.reset_index(inplace = True)
    index_list = ['Player1', 'Player2', 'Player3', 'Player4']
    df_index_list = df['index'].tolist()
    assert index_list == df_index_list

