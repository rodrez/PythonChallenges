filtered_list = []


# This function will remove anything that is not an integer, and every integer will be assigned to a new list.
def filter_list(l):
    for item in l:
        if type(item) == int:
            filtered_list.append(item)
    print(filtered_list)

filter_list([1, 2, 'a', 'b'])
filter_list([1,'a','b',0,15])
filter_list([1,2,'aasf','1','123',123])

