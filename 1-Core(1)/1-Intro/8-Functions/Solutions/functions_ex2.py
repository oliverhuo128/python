# Cupy your code for the 'ask_user_for_age' while loop below:

age = None
def ask_user_for_age():
    s = f'please enter your age: '
    age = input(s)
    return int(age)

while age == None:
    try:
        age = ask_user_for_age()
    except:
        print('Failed to get age from user.')
        age = None

if age !=None:
    print(f'You are {age}')