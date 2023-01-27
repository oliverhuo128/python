class User:

    def __init__(self, username, password): # one special method argument here: 'self'
        self.num_failed_logins = 0
        self.username = username
        self.password = password

    def say_greeting(self):
        print('a Big Hello from the User!')

    def try_login(self, password):
        if password==self.password:
            self.num_failed_logins=0
            return True
        self.num_failed_logins += 1
        return False