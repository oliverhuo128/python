import numpy as np
import pandas as pd


# Delete the following code and write your solution:
def stat_monster(df):
    df['AvgStat'] = df.apply(lambda row: (row['Speed'] + row['Strength'])/2, axis = 1)
    df['MinStat'] = df.apply(lambda row: min(row['Speed'], row['Strength']), axis = 1)
    df['MaxStat'] = df.apply(lambda row: max(row['Speed'], row['Strength']), axis = 1)
    return df


# Once you have written your function, you can test it by running the code below:
if __name__ == '__main__':
    data = {'Name': ['Mike', 'Saly', 'Randall', 'Boo'],
          'Strength': [1,99,35,5],
          'Speed':[3,65,99,5],
          'Type':['Monster', 'Monster', 'EvilMonster', 'Human']}
    test_df = pd.DataFrame(data)
    value = stat_monster(test_df)
    print(value)
