import pandas as pd


# Delete the below code and write your solution
def create_reset_monster(create_monster_lod):  
    df = create_monster_lod()
    df.index = ['Player1', 'Player2', 'Player3', 'Player4']
    return df