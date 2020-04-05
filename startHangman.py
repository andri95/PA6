from hangmanInstance import Hangman

class User:
    def __init__(self, username = 'guest', wins = 0, losses = 0, games = []):
        self.username = username
        self.wins = wins
        self.losses = losses
        self.games = games

class MainMenu:
    def __init__(self):
        self.path = 'users.txt'
        self.users = {}
        self.display = '''
++++++++++++++++++++++++++++++++++++
              HANGMAN 
         +---+    1. Play as guest
         |   |    2. Select user
         O   |    3. Create user
        /|\  |    4. Add words
        / \  |    5. Quit
             |    
     =========

++++++++++++++++++++++++++++++++++++'''
        self.initialize()
        self.start()

    def initialize(self):
        counter = 1
        with open(self.path, 'r') as uf:
            for user in uf:
                self.users[str(counter)] = user.strip()
                counter += 1

    def start(self):
        flag = True
        while flag:
            print(self.display)
            actions = {'1': Hangman, '2': self.select_user, '3': self.create_user, '4': self.add_words}
            action = input('Select option: ')
            if action in actions:
                if action == '1':
                    guest = User()
                    actions[action](guest)
                else:
                    actions[action]()
            elif action == '5':
                    print('Thank you for playing!')
                    flag = False
            else:
                print('Invalid input!')
                self.start()

    def select_user(self):
        print('Users')
        for user in self.users:
            print('{}. {}'.format(user, self.users[user]))

        action = input('Select user: ')
        if action in self.users:
            selectedUser = User()
            with open('{}.txt'.format(self.users[action]), 'r') as uf:
                counter = 0
                selectedUser.username = self.users[action]
                selectedUser.games = []
                for line in uf:
                    if counter == 0:
                        selectedUser.wins = int(line.strip())
                    elif counter == 1:
                        selectedUser.losses = int(line.strip())
                    else:

                        selectedUser.games.append(line.strip())
                    counter += 1
        
            Hangman(selectedUser)
        else:
            print('Invalid input!')
            self.select_user()

    def create_user(self):
        newUser = input('New username: ')
        with open('{}.txt'.format(newUser),'w+') as newUserF:
            newUserF.write('0\n0\n')
        with open(self.path, 'a') as f:
            f.write('\n')
            f.write(newUser)
        self.initialize()
        self.select_user()

    def add_words(self):
        word = input('Enter new word: ')
        for letter in word:
            if not letter.isalpha():
                print('The word must only contain alphabetic letters!')
                self.add_words()
        with open('word_bank.txt', 'a') as wb:
            wb.write('\n' + word)

if __name__ == '__main__':
    MainMenu()