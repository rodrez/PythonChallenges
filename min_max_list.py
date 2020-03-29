# test([1,2,3,4,5], [1,5])
# test([2334454,5], [5, 2334454])

def min_max(lst):
    [a, b] = min(lst), max(lst)
    return [a,b]
print(min_max([1,2,3,4,5]))
