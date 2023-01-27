
# the original function, as used in PY01.01.Intro.08.Functions:
def get_age_from_string(user_input):
    try:
        age = int(user_input)
        if age>=0:
            return age
        else:
            return 'not known'
    except:
        return 'not known'

# In this exercise, we'll write v2. For invalid input, it should
# raises an Exception that includes the messaage 'invalid input' 
def get_age_from_string_v2(user_input):
    pass

def get_age_from_string_v3(user_input):
    pass
