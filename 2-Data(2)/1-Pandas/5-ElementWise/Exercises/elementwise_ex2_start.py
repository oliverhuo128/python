import numpy as np
import pandas as pd



def boost_monster(df):
    pass

# Once you have written your function, you can test it by running the code below:
if __name__ == '__main__':
    data = {'Name': ['Mike', 'Saly', 'Randall', 'Boo'],
          'Strength': [1,99,35,5],
          'Speed':[3,65,99,5],
          'Type':['Monster', 'Monster', 'EvilMonster', 'Human']}
    test_df = pd.DataFrame(data)
    value = boost_monster(test_df)
    print(value)
