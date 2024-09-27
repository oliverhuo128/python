import pandas as pd


# Delete the below code and write your solution
def create_monster_lod():
    data = [{'Name':'Mike', 'Strength':1, 'Speed':3, 'Type':'Monster'},
            {'Name':'Sully', 'Strength':99, 'Speed':65, 'Type':'Monster'},
            {'Name':'Randall', 'Strength':35, 'Speed':99, 'Type':'EvilMonster'},
            {'Name':'Boo', 'Strength':5, 'Speed':5, 'Type':'Human'}]
    df = pd.DataFrame(data)
    return df 