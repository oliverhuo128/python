import numpy as np
import pandas as pd


# Delete the following code and write your solution:
def loc_monster(df):
    fungus_speed = df.loc[90, 'Speed']
    celias_type = df.loc[91, 'Type']
    waternoose_mcode = df.loc[92, 'MCODE']
    loc_values =  {'fungus_speed':fungus_speed, 'celias_type':celias_type, 'waternoose_mcode':waternoose_mcode}
    return loc_values



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