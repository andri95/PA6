from hashmap import HashMap
from linkedlist import LinkedList
import random

class Hangman:
    def __init__(self, user):
        self.user = user
        self.words = HashMap()
        self.highScores = {}
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
        self.start()

    def initialize(self):
        self.wins = int(self.user.wins)
        self.losses = int(self.user.losses)
        self.games = self.user.games
        counter = 0
        with open('word_bank.txt', 'r') as wb:
            for line in wb:
                self.words.insert(counter, line.strip())
                counter += 1
        with open('highScores.txt', 'r') as hs:
            for line in hs:
                temp = line.strip().split(':')
                if temp[2] not in self.highScores:
                    self.highScores[temp[2]] = [[temp[0], temp[1]]]
                else:
                    self.highScores[temp[2]].append([temp[0], temp[1]])
        self.keys = counter - 1

    def start(self):
        while True:
            print(self.display.format(W=self.wins, L=self.losses))
            actions = {'1': self.play, '2': self.set_limit, '3': self.get_highScores, '4': self.get_pastGames, '5': self.add_words}
            action = input('Choose option: ')
            if action in actions:
                actions[action]()

            elif action == '6':
                return

            else:
                print('Invalid input!')

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
                    return self.guessWordCheck(1, score, word_list, word)
                else:
                    return self.guessWordCheck(0, score, word_list, word)
            else:
                if word_list.find(guess) == True:
                    if word_list.reveal_status() == True:
                        return self.guessWordCheck(2, score, word_list, word)
                    else:
                        print('Correct!')
                        score += 1
                else:
                    print('Incorrect!')
                    guesses += 1
                    guessed.append(guess)
 
        return self.guessWordCheck(0, score, word_list, word)
 
    def guessWordCheck(self, check, score, word_list, word):
        if check == 1:
            score += 5
            self.user.wins += 1
            self.wins = self.user.wins
            print('Correct, you won!')
        elif check == 2:
            print('Correct, you won!')
            self.user.wins += 1
            self.wins = self.user.wins
            word_list.reveal_all()
            print('The word was "{}"'.format(word))
        else:
            print('You lost!')
            self.user.losses += 1
            self.losses = self.user.losses
            word_list.reveal_all()
            print('The word was "{}"'.format(word))
       
        self.user.games.append('word = {}, score = {}'.format(word, score))
        self.storeGame(word, score)
        if str(score) not in self.highScores:
            self.highScores[str(score)] = [[self.user.usernamename, word]]
        else:
            self.highScores[str(score)].append([self.user.username, word])

    def storeGame(self, word, score):
        print(self.user.username)
        with open('{}.txt'.format(self.user.username), 'w') as uf:
            uf.write(str(self.user.wins) + '\n')
            uf.write(str(self.user.losses) + '\n')
            for game in self.user.games:
                print(game)
                uf.write(game + '\n')

    def update_highScores(self):
        with open('highScores.txt', 'w') as hs:
            for highScore in sorted(self.highScores):
                if len(self.highScores[highScore]) > 2:
                    for game in self.highScores[highScore]:
                        hs.write('{}:{}:{}\n'.format(self.highScores[highScore][game][0],
                                                        self.highScores[highScore][game][1], highScore))
                else:
                    hs.write('{}:{}:{}\n'.format(self.highScores[highScore][0][0],
                                                            self.highScores[highScore][0][1], highScore))

    def set_limit(self):
        print('Current guess limit: {}'.format(self.guessLimit))
        newLimit = input('Enter new guess limit: ')
        if newLimit.isdigit():
            self.guessLimit = int(newLimit)
        else:
            print('Invalid input!')
            self.set_limit()

    def get_highScores(self):
        for highScore in self.highScores:
            if len(self.highScores[highScore]) > 2:
                for game in self.highScores[highScore]:
                    print('{} {} {}'.format(self.highScores[highScore][game][0],
                                                    self.highScores[highScore][game][1], highScore))
            else:
                print('{} {} {}'.format(self.highScores[highScore][0][0],
                                                        self.highScores[highScore][0][1], highScore))

    def get_pastGames(self):
        print('\n'.join(self.games))

    def add_words(self):
        word = input('Enter new word: ')
        for letter in word:
            if not letter.isalpha():
                print('The word must only contain alphabetic letters!')
                self.add_words()
        with open('word_bank.txt', 'a') as wb:
            wb.write('\n' + word)

    def get_word(self):
        randomKey = random.randint(0, self.keys)
        word_obj = self.words.find(randomKey)
        return self.link_word(word_obj)

    def link_word(self, word_obj):
        word = LinkedList()
        for letter in word_obj.data:
            word.push_back(letter)
        return word, word_obj.data
