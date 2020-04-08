# [12, 10, 8, 12, 7, 6, 4, 10, 12, 10]
from collections import OrderedDict

arr = [8, 13, 12, 10, 8, 12, 7, 6, 4, 10, 12, 10]

def highest_rank(arr):
    return sorted(arr, key=lambda x: (arr.count(x), x))[-1]

    # elements = {}
    #
    # for item in arr:
    #     if item not in elements.keys():
    #         elements[item] = 1
    #     else:
    #         item_count = elements.get(item,0)
    #         elements[item] =item_count + 1
    # arr_dict = OrderedDict(sorted(elements.items(), reverse=True))
    #
    # listOfKeys = max([key  for (key, value) in arr_dict.items() if value == max(arr_dict.values())])
    # return listOfKeys

print(highest_rank(arr))