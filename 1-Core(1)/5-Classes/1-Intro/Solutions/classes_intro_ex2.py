# enter code for Teacher class here
import random

class Teacher:
    def __init__(self):
        self.is_angry = False
        self.is_drunk = False

    def teach(self):
        msg = 'Python is great!'
        if self.is_angry:
            msg = msg.upper()
        if self.is_drunk:
            msg = "".join(random.sample(msg, len(msg)))
        print(msg)
        self.is_angry = True
        return msg

    def drink_booze(self):
        self.is_angry = False
        self.is_drunk= True
        
    def drink_water(self):
        self.is_drunk = False