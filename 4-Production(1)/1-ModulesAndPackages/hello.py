# Save the following content into a file called hello.py
import pandas as pd

# We can make variables for use
my_list = [1,2,3]
my_series = pd.Series(my_list, index = ['a','b','c'])

# We can make functions for use
def make_df(cols, rows):
    data = {c:[str(c)+str(r) for r in rows] for c in cols}
    return pd.DataFrame(data)

# But we should try to minimise the bare code at the global level
my_df = make_df('abc','1234')
print(my_df)

if __name__ == '__main__':
    print(f'__name__ is {__name__}' )
    print('This file is running as a script')
else:
    print(f'__name__ is {__name__}' )
    print('This file is running as a module')