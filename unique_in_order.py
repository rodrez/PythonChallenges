# Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any
# elements with the same value next to each other and preserving the original order of elements.


def unique_in_order(iterable):
    my_list = [i for i in iterable]
    new_list = []

    # Used a for loop to only append items that were not equal to the last item in the list
    for item in my_list:
        if len(new_list) == 0:
            new_list.append(item)
        elif len(new_list) > 0:
            if new_list[-1] != item:
                new_list.append(item)
    print(new_list)


unique_in_order('AAAABBBCCDAABBB')
unique_in_order('ABBCcAD')
unique_in_order([1,2,2,3,3])
unique_in_order([])
unique_in_order('Aa')