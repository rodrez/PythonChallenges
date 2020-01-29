import random


game_words = ['rock', 'paper', 'scissors']
computer_pick = random.choice(game_words)


def player_choice(r='Rock', p='Paper', s='Scissors'):
    while True:
        choice = input('Select R for Rock, P for Paper and S for Scissors.').upper()

        if choice[0] == 'R':
            return r
            break
        elif choice[0] == 'P':
            return p
            break
        elif choice[0] == 'S':
            return s
            break


def win_check(user_choice, computer_choice):
    if user_choice == 'Rock' and computer_choice == 'Scissors':
        print('The player has won.')
    elif user_choice == 'Paper' and computer_choice == 'Rock':
        print('The player has won.')
    elif user_choice == 'Scissors' and computer_choice == 'Paper':
        print('The player has won.')
    elif user_choice == 'Rock' and computer_choice == 'Paper':
        print('The computer has won.')
    elif user_choice == 'Paper' and computer_choice == 'Scissors':
        print('The computer has won.')
    elif user_choice == 'Scissors' and computer_choice == 'Rock':
        print('The computer has won.')


def replay():
    return input('Would you like to play another game?').lower().startswith('y')


# Game Play

while True:
    print('Welcome to Rock, Paper and Scissors.')

    game_start = input('Ready to start the game?').lower().startswith('y')

    print('Time to game!')
    player_pick = player_choice()
    win_check(player_pick, computer_pick)

    if not game_start:
        break
