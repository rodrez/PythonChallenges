currency = {'dollar': 100, 'quarters': 25, 'dime': 10, 'nickel': 5, 'pennies': 1}
amount = int(input('Please insert your change in the machine.'))

print(f'Hello!, you inserted {amount}')

dollar = amount // currency['dollar']
reminder = amount % 100

quarter = reminder // currency['quarters']
reminder = reminder % 25

dime = reminder // currency['dime']
reminder = reminder % 10

nickel = reminder // currency['nickel']
reminder = reminder % 5

pennie = reminder // currency['pennies']
reminder = reminder % 1
print(f'\nHello! you change would be {dollar} dollars, {quarter} quarters, {dime} dimes, {nickel}, nickels, and {pennie} pennies.'
      f'\nThanks for doing your transactions with Rodrez Ltd.')