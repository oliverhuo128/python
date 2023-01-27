# The 'exercises' copy of this file should have these three functions:

def salmon( skin, hoisin = 'no'):
    return f'Getting you a Salmon, with {skin} skin and {hoisin} hoisin sauce'

def duck( how, sauce='orange'):
    return f'Getting you a Duck, {how}, with a {sauce} sauce'

def tofu(soy = 'plenty'):
    return f'Getting you a Tofu with {soy} of soy sauce'

# Here is the solution

def process_order(dish_to_prepare, **kwargs):
    return dish_to_prepare(**kwargs) 
                     