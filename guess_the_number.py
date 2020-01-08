# Author: Fabian Rodriguez

import random

print('Welcome to Guess the number game!')
print('Try to guess a random number from 1 to 20')

# Use the random library to decide a random number between 1-20
random_number = random.randint(1, 20)

# Game Logic
player_choice = ''
while player_choice != random_number:
    player_choice = int(input('Select a number from 1-20\n'))
    if player_choice > random_number:
        print('Your number is greater than the random number!')
    elif player_choice < random_number:
        print('Your number is less than the random number.')
    elif player_choice == random_number:
        print('Congratulations you guess the number!')
        break
# TODO: Add more features
