# sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]
def sort_array(source_array):
    # Return a sorted array.
    lst = sorted(source_array)
    for idx, i in enumerate(source_array):
        if i % 2 == 0:
            lst.remove(i)
            lst.insert(idx, i)
    return lst
print(sort_array([5, 3, 1, 8, 0]))
