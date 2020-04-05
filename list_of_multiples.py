def list_of_multiples (num, length):
	return [num*idx for idx, number in enumerate(range(length+1)) if number != 0]

print(list_of_multiples(7,5))
