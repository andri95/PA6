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
        / \  |    5. Add words
             |    6. Quit
     =========
          Wins: {W} Losses: {L}
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
        print(self.display.format(W=self.wins, L=self.losses))
        actions = {'1': self.play, '2': self.set_limit, '3': self.get_highScores, '4': self.get_pastGames, '5': self.add_words, '6': self.quit}
        action = input('Choose option: ')
        if action in actions:
            actions[action]()

        else:
            print('Invalid input!')
            self.start()

    def play(self):
        guessed = []
        guesses = 0
        word_list, word = self.get_word()
        while guesses <= self.guessLimit:
            print('\nGuessed letters: {} Guesses left: {}'.format(', '.join(guessed), (self.guessLimit - guesses)))
            print(word_list)
            guess = input('Input letter: ')
            if len(guess) > 1:
                if guess == word:
                    self.wins += 1
                    print('Correct, you won!')
                    self.start()
                else:
                    print('Incorrect, you lost!')
                    self.losses += 1
                    word_list.reveal_all()
                    print('The word was "{}"'.format(word))
                    self.start()
            else:
                if word_list.find(guess) == True:
                    if word_list.reveal_status() == True:
                        print('Correct, you won!')
                        self.wins += 1
                        word_list.reveal_all()
                        print('The word was "{}"'.format(word))
                        self.start()
                    else:
                        print('Correct!')
                else:
                    print('Incorrect!')
                    guesses += 1
                    guessed.append(guess)

        print('You lost!')
        self.losses += 1
        word_list.reveal_all()
        print('The word was "{}"'.format(word_list))
        self.start()

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
        pass

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
        print('Thank you for playing!')

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