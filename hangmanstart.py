#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from hangmangame import Galley

def hangman(word_length):
    """The program that starts hangman"""
    if word_length < 1:
        return 'STOP TRYING TO BREAK THE SYSTEM! ENTER GREATER THAN ZERO!'
    if word_length > 13:
        return 'STOP TRYING TO BREAK THE SYSTEM! ENTER LESS THAN 13!'
    galley = Galley(word_length)
    print(galley.word)
    while galley.alive_status() == True:
        print(galley)
        print('Enter a letter: ')
        guess = input()
        while guess.isalpha() != True:
            print('Enter a valid input! ')
            guess = input()
        guess = guess.lower()
        galley.add_correct_letters(guess)
        if galley.win_status() == True:
            print(galley)
            return 'THE WORD WAS: ' + galley.word + '. YOU WON AND LIVE TO SEE ANOTHER DAY'
    if galley.alive_status() == False:
        print(galley)
        return 'THE WORD WAS: ' + galley.word +'. YOU HAVE LOST HEHE'
        
