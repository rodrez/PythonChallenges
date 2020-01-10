import random

# This will be a dictionary that can pull different random words
bunch_of_words = ['hello', 'poopoo']
word = random.choice(bunch_of_words)

# Converts the word to a secret word
secret_word = ['_'] * len(word)

print(secret_word)


# def replay():
#   return input('Would you like to play another game?').lower().startswith('y')


# Keeps the game running until the break happens
failed_attempts = 0
used_letters = []

while failed_attempts != 6:
    chosen_letter = input('Enter a letter from A to Z:')
    # Use enumerate to iterate trough the word and get the index position and the letter
    for i, char in enumerate(word):
        if chosen_letter == char:
            secret_word[i] = char
        # Adds the chosen letter to the list that way the user can't repeat the same letters
            used_letters.append(chosen_letter)
            print(f'A new letter was added to the secret word \n {secret_word}')
    # Check is the user won the game!
    if ''.join(secret_word) == word:
        break
    elif chosen_letter not in word:
        failed_attempts += 1
        used_letters.append(chosen_letter)
        print(f'The amount of turns left is {6 - failed_attempts}')

else:
    print("You have been hanged!")