import numpy as np
import pandas as pd



def combine_monster(df1, df2, df3):
    pass



# Once you have written your function, you can test it by running the code below:
if __name__ == '__main__':
    data1 = {'Name': ['Mike', 'Saly', 'Randall', 'Boo'],
          'Strength': [1,99,35,5],
          'Speed':[3,65,99,5],
          'Type':['Monster', 'Monster', 'EvilMonster', 'Human']}
    test_df1 = pd.DataFrame(data1)
    data2 = {'Name': ['Fungus', 'Celia', 'Waternoose'],
        'Strength': [np.nan, 40,51],
        'Speed':[3, np.nan, 35],
        'Type':['Monster', 'Monster', 'EvilMonster'],
        'Color':['Orange', 'Purple', 'Gray'],
        'MCODE':[223423, 223422, 223234]}
    test_df2 = pd.DataFrame(data2, index = [90,91,92])
    data3 = {'Species':['Monster', 'Human', 'EvilMonster', 'Donut'],
          'FavouriteFood':['Screams', 'Candy', np.nan, 'Flour']}
    test_df3 = pd.DataFrame(data3) 
    value = combine_monster(test_df1, test_df2, test_df3)
    print(value)
