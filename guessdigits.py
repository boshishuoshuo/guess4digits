# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 12:38:02 2017

@author: Yan.Feng
"""

import random
import string

def chooseNumber():
    digits_List = list(string.digits)
    return ''.join(random.sample(digits_List, 4))

def goodInput(s):
    if len(set(s)) == 4 and set(s).issubset(set(string.digits)):
        return True
    else:
        return False

def isCorrect(Number_to_guess, Number_guessed):
    a = 0
    Number_guessed_list = list(Number_guessed)
    for i in range(4):
        if Number_to_guess[i] == Number_guessed[i]:
            a += 1
            Number_guessed_list.remove(Number_guessed[i])
    b = len(set(Number_guessed_list).intersection(set(Number_to_guess)))
    return {'A': a, 'B': b}

def guess4digits(Number_to_guess):
    print('''\nWelcome to the game: guess 4 digits! \n
There is a 4-digit number you need to guess. For each time, you input 
a guess of a 4-digit number. You'll see the response, A: a digit, B: 
a digit. A counts the number if both the digit and position are correct, 
while B counts the number if only digit is correct. You will repeat 
until you get the correct answer or reach 20 tries.\n''')
    print('Game starts: here is a 4-digit number you need to guess.')
    #print(Number_to_guess)
    trial = 1
    response = {}
    while trial <= 21:
        print('--------------------')
        if trial == 21:
            print('You have tried 20 times and you lose the game!')
            break
        else:
            guess = input('Please guess a 4-digit number: ')
            while not goodInput(guess):
                print('Wrong input!')
                guess = input('Please guess a 4-digit number: ')
            if guess in response:
                print('You have already guessed that number.')
            else:
                response[guess] = isCorrect(Number_to_guess, guess)
                if response[guess]['A'] != 4:        
                    print('Response: ', isCorrect(Number_to_guess, guess))
                    print('You have tried %d times.' % trial)
                    trial += 1
                else:
                    print('Congratulation!')
                    print('You guessed the number in %d times' % trial)
                    break
    
number_to_guess = chooseNumber()    
guess4digits(number_to_guess)
    
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
    