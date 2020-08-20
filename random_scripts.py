import string 

def alpha_letters(numbers=True):
    letters_dict = {}

    # Creates an alphabet dictionary from the string module
    for number, letter in enumerate(string.ascii_lowercase):
        
        if len(str(number)) < 2:
            letters_dict["0" + str(number + 1)] = letter

        else:
            letters_dict[str(number + 1)] = letter

    return letters_dict


# print(alphabet_creator())

def crypto_letters(crypto_number):
    """summary

    Args:
        crypto_number (int): A number that will be converted to letters
    """

    # Indicates the nth number to create the pairsMM
    n = 2 

    # List comp to create the pairs
    pairs = [str(crypto_number)[i:i+n] for i in range(0, len(str(crypto_number)), n)]
    # Works

    alpha = alphabet_creator()

    word = []

    for pair in pairs:
        for letter, number in alpha.items():
            if pair == letter:
                word.append(alpha[letter])

    return "".join(word)

# print(crypto_letters(20052420))

def crypto_numbers(crypto_word):
    
    alpha = alphabet_creator()

    word_in_num = []

    for l in crypto_word:
        for number, letter in alpha.items():
            if l == letter:
                word_in_num.append(alpha[number]) 
            
    return "".join(word_in_num)

print(crypto_numbers("text"))