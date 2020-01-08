import random

# This will be a dictionary that can pull different random words
bunch_of_words = ['hello', 'poopoo']
word = random.choice(bunch_of_words)

# Converts the word to a secret word
secret_word = ['_'] * len(word)

print(secret_word)

# Keeps the game running until the break happens
while True:
    chosen_letter = input('Enter a letter from A to Z:')
    used_letters = []
    failed_attempts = 0

    # Use enumerate to iterate trough the word and get the index position and the letter
    for i, char in enumerate(word):
        if chosen_letter == char:
            secret_word[i] = char
        # Adds the chosen letter to the list that way the user can't repeat the same letters
        # TODO: used_letters.append(chosen_letter)
            print(f'A new letter was added to the secret word \n {secret_word}')

    # Check is the user won the game!
    if ''.join(secret_word) == word or failed_attempts == 6:
        break
    elif chosen_letter not in word:
        failed_attempts += 1
        print(f'The amount of turns left is {6 - failed_attempts}')
