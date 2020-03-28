# SeriesSum(1) => 1 = "1.00"
# SeriesSum(2) => 1 + 1/4 = "1.25"
# SeriesSum(5) => 1 + 1/4 + 1/7 + 1/10 + 1/13 = "1.57"

def series_sum(n):
    fraction = 4
    base_number = 1
    for i in range(int(n)-1):
        if n > 1:
            base_number += (1/fraction)
            fraction += 3
    if n < 1:
        return "0.00"
    elif n == 1:
        return "1.00"
    else:
        return '{:0.2f}'.format(base_number)


print(series_sum(44))

# return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n))
