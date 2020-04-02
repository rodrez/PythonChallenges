inputArray = [-2, 2, 5, -11, 6]

def max_sequence(arr):
    max_sum = 0
    current_sum = 0

    for idx, i in enumerate(arr):
        # We use enumerate to keep track of the index

        current_sum = max(arr[idx] + current_sum, arr[idx])
        # We use the max to decide if the element at idx +
        # the current sum is greater than the arr at idx location

        max_sum = max(current_sum, max_sum)
        # returns the greater value from current sum and max_sum
        # and assigns that value to max_sum

    return max_sum
