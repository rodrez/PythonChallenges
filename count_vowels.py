#Count Vowels

word = 'Notebook'
vowels = ['a', 'e', 'i', 'o', 'u']

vowels_in_word = [letter for letter in word if letter in vowels]
print(len(vowels_in_word))

breakpoint()

vowels_dict = {'a':0, 'e':0,'i':0,'o':0,'u':0}
for char in word:
      if char in vowels:
            vowels_dict[char] += 1
print(vowels_dict)

breakpoint()
