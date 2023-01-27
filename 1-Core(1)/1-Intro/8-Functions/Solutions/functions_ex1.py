# copy in your functions 'get_full_name' and 'get_age_from_string' below:

def get_full_name(first, second):
    return first + ' ' + second

def get_age_from_string(age):
    try:
        int(age)
    except ValueError:
        age = None
    if age == None or int(age) < 0:
        return("not known")
    else:
        return int(age)

