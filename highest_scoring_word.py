# ('man i need a taxi up to ubud'), 'taxi')
def high(x):
    word_dict = {}

    for word in x.split():
        word_sum = 0
        for letter in word:
            word_sum += (ord(letter)-96)
        word_dict[word] = word_sum
    word_max = max(word_dict.values())
    word = ([key for (key, value) in word_dict.items() if value == word_max])[0]
    print(word_dict)
    return word
