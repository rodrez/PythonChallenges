text = "aabBcde"

def duplicate_count(text):

    new_list = []
    counter = 0
    already_counted = []
    for char in text:
        if char.lower() not in new_list:
            new_list.append(char)
        else:
            if char.lower() not in already_counted:
                counter += 1
                already_counted.append(char)


    return counter

print(duplicate_count(text))
