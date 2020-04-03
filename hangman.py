from hashmap import HashMap
from linkedlist import LinkedList
import random

class Hangman:
    def __init__(self):
        self.words = HashMap()
        self.games = LinkedList()
        self.wins = 0
        self.losses = 0
        self.guessLimit = 6
        self.keys = 0
        self.display = '''
++++++++++++++++++++++++++++++++++++
              HANGMAN
         +---+    1. Play
         |   |    2. Set guess limit
         O   |    3. High scores
        /|\  |    4. Past games
        / \  |
             |
     =========
++++++++++++++++++++++++++++++++++++'''
        self.initialize()
        self.start()

    def initialize(self):
        counter = 0
        with open('word_bank.txt', 'r') as wb:
            for line in wb:
                self.words.insert(counter, line.strip())
                counter += 1
        self.keys = counter + 1

    def start(self):
        print(self.display)
        actions = {'1': self.play, '2': self.set_limit, '3': self.get_highScores, '4': self.get_pastGames}
        action = input('Choose option: ')
        if action in actions:
            actions[action]()

        else:
            print('Invalid input!')
            self.start()

    def play(self):
        self.get_word()

    def set_limit(self):
        pass

    def get_highScores(self):
        pass

    def get_pastGames(self):
        pass

    def get_word(self):
        randomKey = random.randint(0, self.keys)
        word = self.words.find(randomKey)
        print(word)


if __name__ == '__main__':
    Hangman()