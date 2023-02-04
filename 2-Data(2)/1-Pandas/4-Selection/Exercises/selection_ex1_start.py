import numpy as np
import pandas as pd
import pickle


def loc_monster(df):
    pass



# Once you have written your function, you can test it by running the code below:
if __name__ == '__main__':
    data = {'Name': ['Fungus', 'Celia', 'Waternoose'],
            'Strength': [np.nan, 40,51],
            'Speed':[3, np.nan, 35],
            'Type':['Monster', 'Monster', 'EvilMonster'],
            'Color':['Orange', 'Purple', 'Gray'],
            'MCODE':[223423, 223422, 223234]}
    test_df = pd.DataFrame(data, index = [90,91,92])
    value = loc_monster(test_df)
    print(value)