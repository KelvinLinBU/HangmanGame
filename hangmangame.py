#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random

class Galley:
    """class that represents the galley"""
    
    def __init__(self, word_length):
        """class constructor"""
        self.word_length = word_length
        self.word = self.choose_word()
        self.guess_progress = []
        for length in range(word_length):
            self.guess_progress += [[]]
        self.lives = 6
        self.wrong_guesses = ''
        
    def __repr__(self):
        """Returns a string that represents the galley object"""
        if self.lives == 6:
            s = '    -----T  YOUR GUESS' + "\n"
            s += '    |    |  '  
            for x in range(self.word_length):
                s += str(self.guess_progress[x])
            s += '\n'
            s += '         |' + "\n"
            s += '         |' + '  WRONG GUESSES' + "\n"
            s += '         |  ' + self.wrong_guesses + "\n"
            s += '         |' + "\n"
            s += '[------------]' + "\n"
            s += '  The Galley' + "\n"
            s += '  '
        if self.lives == 5:
            s = '    -----T  YOUR GUESS' + "\n"
            s += '    |    |  '
            for x in range(self.word_length):
                s += str(self.guess_progress[x])
            s += '\n'
            s += '    O    |' + "\n"
            s += '         |' + '  WRONG GUESSES' + "\n"
            s += '         |  ' + self.wrong_guesses + "\n"
            s += '         |' + "\n"
            s += '[------------]' + "\n"
            s += '  The Galley' + "\n"
            s += '  '
        if self.lives == 4:
            s = '    -----T  YOUR GUESS' + "\n"
            s += '    |    |  '
            for x in range(self.word_length):
                s += str(self.guess_progress[x])
            s += '\n'
            s += '    O    |' + "\n"
            s += '    |    |' + '  WRONG GUESSES' + "\n"
            s += '         |  ' + self.wrong_guesses + "\n"
            s += '         |' + "\n"
            s += '[------------]' + "\n"
            s += '  The Galley' + "\n"
            s += '  '
        if self.lives == 3:
            s = '    -----T  YOUR GUESS' + "\n"
            s += '    |    |  '
            for x in range(self.word_length):
                s += str(self.guess_progress[x])
            s += '\n'
            s += '    O    |' + "\n"
            s += '   -|    |' + '  WRONG GUESSES' + "\n"
            s += '         |  ' + self.wrong_guesses + "\n"
            s += '         |' + "\n"
            s += '[------------]' + "\n"
            s += '  The Galley' + "\n"
            s += '  '
        if self.lives == 2:
            s = '    -----T  YOUR GUESS' + "\n"
            s += '    |    |  '
            for x in range(self.word_length):
                s += str(self.guess_progress[x])
            s += '\n'
            s += '    O    |' + "\n"
            s += '   -|-   |' + '  WRONG GUESSES' + "\n"
            s += '         |  ' + self.wrong_guesses + "\n"
            s += '         |' + "\n"
            s += '[------------]' + "\n"
            s += '  The Galley' + "\n"
            s += '  '
        if self.lives == 1:
            s = '    -----T  YOUR GUESS' + "\n"
            s += '    |    |  '
            for x in range(self.word_length):
                s += str(self.guess_progress[x])
            s += '\n'
            s += '    O    |' + "\n"
            s += '   -|-   |' + '  WRONG GUESSES' + "\n"
            s += '   /     |  ' + self.wrong_guesses + "\n"
            s += '         |' + "\n"
            s += '[------------]' + "\n"
            s += '  The Galley' + "\n"
            s += '  '
        if self.lives == 0:
            s = '    -----T  YOUR GUESS' + "\n"
            s += '    |    |  ' 
            for x in range(self.word_length):
                s += str(self.guess_progress[x])
            s += '\n'
            s += '    O    |' + "\n"
            s += '   -|-   |' + '  WRONG GUESSES' + "\n"
            s += '   / \   |  ' + self.wrong_guesses + "\n"
            s += '         |' + "\n"
            s += '[------------]' + "\n"
            s += '  The Galley' + "\n"
            s += '  '
        return s
    
    def choose_word(self):
        """chooses a random word of chosen length"""
        word = random.choice(open('wordlist.10000.txt').read().split()).strip()
        while len(word) != self.word_length:
            word = random.choice(open('wordlist.10000.txt').read().split()).strip()
        return word
    
    def guess_accuracy(self, letter_guess):
        """takes one letter, and return true if it is in the word, and false if it is not"""
        if letter_guess in self.word:
            return True
        return False
    
    def add_correct_letters(self, letter_guess):
        """adds correct letters to guess_progress"""
        if self.valid_guess(letter_guess) == False:
            print('You need to put in a valid input!')
            return -1
        guess = self.valid_guess(letter_guess)
        if self.guess_accuracy(guess) == True:
            for x in range(len(self.guess_progress)):
                if letter_guess == self.word[x]:
                    self.guess_progress[x] = letter_guess
        else:
            self.wrong_guesses += letter_guess
            self.lives -= 1
            
    def alive_status(self):
        """checks if you're still alive"""
        if self.lives == 0:
            return False
        return True
    
    def valid_guess(self, letter_guess):
        """checks if guess is valid, and lower cases it"""
        if letter_guess.isalpha() == False:
            return False
        if len(letter_guess) != 1:
            return False
        return letter_guess.lower()
    
    def win_status(self):
        """checks to see if the user has won or not"""
        for x in range(self.word_length):
            if self.guess_progress[x] == []:
                return False
        return True
                    
    
        
        
    
    
    
    
    
    
    
    
    
    