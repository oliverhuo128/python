# enter code for Dog class with get_age_in_dog_years method

class Dog:
    def __init__(self, colour, age):
        self.colour = colour
        self.age    = age
        
    def bark(self):
        print('Woof!')
        return 'Woof!'
        
    def is_old(self):
        return self.age > 10

    def get_age_in_dog_years(self):
        return self.age * 7