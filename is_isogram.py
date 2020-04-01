word = 'moOse'

def is_isogram(string):
    return len(set(string.lower())) == len(string)
    # 1st we convert the string to lowercase using .lower()
    # 2nd we used a set to remove duplicate letters if any existed.
    # 3rd we compare if the length of both elements is the same then
    # by default it will return true, otherwise it will return
    # because the set removed the duplicate characters making the first
    # element shorter than the second element.
print(is_isogram(word))
