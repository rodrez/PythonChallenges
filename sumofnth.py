def arith(first_num, step, nth):
    """
    Uses the pattern given an returns the sum of the nth number
    :param first_num: First integer
    :param step: Step increments
    :param nth: Times of increments
    :return: sum of the nth number
    """
    all_num = [first_num,]
    saved_num = 9
    for i in range(nth-1):
        temp_num = saved_num + step
        saved_num = temp_num
        all_num.append(temp_num)


    return all_num

result = arith(9, 5, 23)
print(sum(result))
