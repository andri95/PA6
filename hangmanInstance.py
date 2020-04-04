from hashmap import HashMap
from linkedlist import LinkedList
import random

class Hangman:
    def __init__(self, user):
        self.user = user
        self.words = HashMap()
        self.guessLimit = 6
        self.keys = 0
        self.display = '''
++++++++++++++++++++++++++++++++++++
              HANGMAN 
         +---+    1. Play
         |   |    2. Set guess limit
         O   |    3. High scores
        /|\  |    4. Past games
        / \  |    5. Add words
             |    6. Log out
     =========
          Wins: {W} Losses: {L}
++++++++++++++++++++++++++++++++++++'''
        self.initialize()

    def initialize(self):
        self.wins = int(self.user.wins)
        self.losses = int(self.user.losses)
        self.games = self.user.games
        counter = 0
        with open('word_bank.txt', 'r') as wb:
            for line in wb:
                self.words.insert(counter, line.strip())
                counter += 1
        self.keys = counter + 1
        self.start()

    def start(self):
        print(self.display.format(W=self.wins, L=self.losses))
        actions = {'1': self.play, '2': self.set_limit, '3': self.get_highScores, '4': self.get_pastGames, '5': self.add_words}
        action = input('Choose option: ')
        if action in actions:
            actions[action]()

        elif action == '6':
            return

        else:
            print('Invalid input!')
            self.start()

    def play(self):
        guessed = []
        guesses = 0
        score = 0
        word_list, word = self.get_word()
        while guesses <= self.guessLimit:
            print('\nGuessed letters: {} Guesses left: {}'.format(', '.join(guessed), (self.guessLimit - guesses)))
            print(word_list)
            guess = input('Input letter: ')
            if len(guess) > 1:
                if guess == word:
                    self.user.wins += 1
                    score += 5
                    print('Correct, you won!')
                    self.user.games.append('word = {}, score = {}'.format(word, score))
                    self.storeGame('W', word, score)
                    self.start()
                else:
                    print('Incorrect, you lost!')
                    self.user.losses += 1
                    word_list.reveal_all()
                    print('The word was "{}"'.format(word))
                    self.user.games.append('word = {}, score = {}'.format(word, score))
                    self.storeGame('L', word, score)
                    self.start()
            else:
                if word_list.find(guess) == True:
                    if word_list.reveal_status() == True:
                        print('Correct, you won!')
                        self.user.wins += 1
                        word_list.reveal_all()
                        print('The word was "{}"'.format(word))
                        self.user.games.append('word = {}, score = {}'.format(word, score))
                        self.storeGame('W', word, score)
                        self.start()
                    else:
                        print('Correct!')
                        score += 1
                else:
                    print('Incorrect!')
                    guesses += 1
                    guessed.append(guess)

        print('You lost!')
        self.user.losses += 1
        word_list.reveal_all()
        print('The word was "{}"'.format(word_list))
        self.user.games.append('word = {}, score = {}'.format(word, score))
        self.storeGame('L', word, score)
        self.start()

    def storeGame(self, winLoss, word, score):
        with open('{}.txt'.format(self.user.username), 'w') as uf:
            uf.write(str(self.user.wins) + '\n')
            uf.write(str(self.user.losses) + '\n')
            for game in self.user.games:
                uf.write(game + '\n')

    def set_limit(self):
        print('Current guess limit: {}'.format(self.guessLimit))
        newLimit = input('Enter new guess limit: ')
        if newLimit.isdigit():
            self.guessLimit = newLimit
            self.start()
        else:
            print('Invalid input!')
            self.set_limit()

    def get_highScores(self):
        pass

    def get_pastGames(self):
        print('\n'.join(self.games))
        self.start()

    def add_words(self):
        word = input('Enter new word: ')
        for letter in word:
            if not letter.isalpha():
                print('The word must only contain alphabetic letters!')
                self.add_words()
        with open('word_bank.txt', 'a') as wb:
            wb.write('\n' + word)
        self.start()

    def quit(self):
        return

    def get_word(self):
        randomKey = random.randint(0, self.keys)
        word_obj = self.words.find(randomKey)
        return self.link_word(word_obj)

    def link_word(self, word_obj):
        word = LinkedList()
        for letter in word_obj.data:
            word.push_back(letter)
        return word, word_obj.data


if __name__ == '__main__':
    Hangman()