# Create a function that takes a string and returns the number (count) of vowels contained within it.
#
# Examples
# count_vowels("Celebration") ➞ 5
#
# count_vowels("Palm") ➞ 1
#
# count_vowels("Prediction") ➞ 4



def count_vowels(txt):

    return sum([1 for x in txt.lower() if x in 'aeiou'])

    # vowels = ['a', 'e', 'i', 'o', 'u']
    # v = 0
    # for i in txt:
    #     if i in vowels:
    #         v += 1
    # return v

print(count_vowels("Celebration"))
