#Python's Random Game Night
#Objective: The aim of this assignment is to explore the random package in Python and understand how it can be used with loops to introduce randomness 
#into your programs.
#Task 1: Random Choice Game Create a game where a player has a list of items. They have to guess which item in the list was selected. 
#Use random.choice() to select the item and take the user's guess via input. Provide feedback on whether they guessed correctly or not keep 
#them playing until they guess correctly.

import random

game = ['Big Butts', 'Big Boobs', 'Personality']

while True:
    my_choice = input('What is the perfect girl ? Big Butts,Big Boobs,or Personality' )
    Alpha = random.choice(game)
    print('Brian chose :', Alpha)
    win = input('Did you win? yes or no ')
    if win == 'yes':
        print('Very wise decision!')
        print('indeed!', my_choice,'beats', Alpha)
        break
