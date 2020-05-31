change = .41

quarter = .25
dime = .10
nickel = .05
pennie = .01

coins = 0


while change != 0:

  if change == 0:
    break

  else:
    if change - quarter > 0:
      change -= quarter
      coins += 1
      print(f"{change:.2f}")
      print(f'Coins: {coins}')

    elif change - dime > 0:
      change -= dime
      coins += 1
      print(f"{change:.2f}")
      print(f'Coins: {coins}')

    elif change - nickel > 0:
      change -= nickel
      coins += 1
      print(f"{change:.2f}")
      print(f'Coins: {coins}')

    elif change - pennie > -.01:
      change -= pennie
      coins += 1
      print(f"{change:.2f}")
      print(f'Coins: {coins}')
