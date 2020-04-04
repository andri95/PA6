from hangmanInstance import Hangman

class User:
    def __init__(self):
        self.path = 'users.txt'
        self.users = {}
        self.display = '''
++++++++++++++++++++++++++++++++++++
              HANGMAN 
         +---+    1. Play as guest
         |   |    2. Select user
         O   |    3. Create user
        /|\  |    4. Quit
        / \  |    
             |    
     =========

++++++++++++++++++++++++++++++++++++'''
        self.initialize()
        self.start()

    def initialize(self):
        counter = 1
        with open(self.path, 'r') as uf:
            for user in uf:
                self.users[str(counter)] = user

    def start(self):
        print(self.display)
        actions = {'1': Hangman, '2': self.select_user, '3': self.create_user, '4': self.quit}
        action = input('Select option: ')
        if action in actions:
            actions[action]()
        else:
            print('Invalid input!')
            self.start()

    def select_user(self):
        print('Users')
        for user in self.users:
            print('{}. {}'.format(user, self.users[user]))

        action = input('Select user: ')
        if action in self.users:
            with open(self.users[action] + '.txt', 'r') as uf:
                pass

    def create_user(self):
        pass

    def quit(self):
        print('Thank you for playing!')

if __name__ == '__main__':
    User()