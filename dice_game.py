def dice_game(lst):
  total = 0
  for num in lst:
    if num[0] == num[1]:
      total = 0
      break
    else:
      total += sum(num)
  return total
