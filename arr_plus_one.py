# For example the array [2, 3, 9] equals 239, adding one would return the array [2, 4, 0].

def up_array(arr):

    li = [i for i in arr if i < 0 or i > 9]
    if li: return None
    else:
        arr = ''.join([str(i) for i in arr])
        new_li = int(arr) + 1
        result = [int(num) for num in str(new_li)]
        return result

print(up_array([1,1,10]))
