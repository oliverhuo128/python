import numpy as np
import pandas as pd


# Delete the following code and write your solution:
def boost_monster(df):
    df['BoostSpeed'] = df.apply(lambda row: 2*row['Speed'] if row['Type']== 'Monster' else row['Speed'], axis = 1)
    df['BoostStrength'] = df.apply(lambda row: 3*row['Strength'] if row['Type']== 'EvilMonster' else row['Strength'], axis = 1)
    return df


# Once you have written your function, you can test it by running the code below:
if __name__ == '__main__':
    data = {'Name': ['Mike', 'Saly', 'Randall', 'Boo'],
          'Strength': [1,99,35,5],
          'Speed':[3,65,99,5],
          'Type':['Monster', 'Monster', 'EvilMonster', 'Human']}
    test_df = pd.DataFrame(data)
    value = boost_monster(test_df)
    print(value)
