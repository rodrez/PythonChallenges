num = 927365184

def descending_order(num):
    return int("".join(sorted(str(num), reverse=True)))
    # 1st we use str to convert the integer to string
    # 2nd we use sorted to sort the numbers. Ascending to descending
    # Note: sorted returns a list
    # 3rd  we add reverse in sorted to reverse the sorting. Descending to ascending
    # 4th we use join to converts the list element to a string
    # 5th we use int to convert the string back to integer.
print(descending_order(num))
