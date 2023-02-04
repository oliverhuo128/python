import pandas as pd


# Delete the below code and write your solution:
def create_monster_lol():
    data = [['Mike', 1, 3, 'Monster'],
            ['Sully', 99, 65, 'Monster'],
            ['Randall', 35, 99, 'EvilMonster'],
            ['Boo', 5, 5, 'Human']]
    df = pd.DataFrame(data, columns = ['Name', 'Strength', 'Speed', 'Type'])
    return df