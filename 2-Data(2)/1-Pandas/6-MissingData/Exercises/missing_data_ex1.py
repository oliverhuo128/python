import numpy as np
import pandas as pd


# Delete the following code and write your solution
def interpolate_monster(df):
    df = df.interpolate()
    df = df.dropna(axis = 0)
    return df


# Once you have written your function, you can test it by running the code below:
if __name__ == '__main__':
    data = {'Name': ['Fungus', 'Celia', 'Waternoose'],
        'Strength': [np.nan, 40,51],
        'Speed':[3, np.nan, 35],
        'Type':['Monster', 'Monster', 'EvilMonster'],
        'Color':['Orange', 'Purple', 'Gray'],
        'MCODE':[223423, 223422, 223234]}
    test_df = pd.DataFrame(data, index = [90,91,92])
    value = interpolate_monster(test_df)
    print(value)
