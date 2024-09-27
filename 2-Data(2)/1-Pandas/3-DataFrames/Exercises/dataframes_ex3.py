import pandas as pd


# Delete the below code and write your solution
def create_monster_dol():
    data = {'Name': ['Mike', 'Saly', 'Randall', 'Boo'],
          'Strength': [1,99,35,5],
          'Speed':[3,65,99,5],
          'Type':['Monster', 'Monster', 'EvilMonster', 'Human']}
    df = pd.DataFrame(data)
    return df