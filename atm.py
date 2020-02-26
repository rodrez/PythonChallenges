# Global Variable to hold the account balance
account_balance = round(float(500.25),2)

# Outputs the account balance to the user
def balance():

  # Use the global function to access the account variable outside the function scope
  global account_balance
  print(f'Your account balance is {account_balance}.')

# deposit function
def deposit(amount):
  # Use the global function to access the account variable outside the function scope
  global account_balance
  # Short for account_balance = account_balance + amount
  account_balance += amount
  return account_balance

# withdraw function
def withdrawal(amount):
  # Use the global function to access the account variable outside the function scope
  global account_balance
  # Short for account_balance = account_balance - amount
  account_balance -= amount
  return account_balance

# Created exiting variable to end the while loop
exiting = True

# Added while to keep the ATM Service running until the user decides to stop.
while exiting:

  # Request user input of desired action.
  user_choice = input("What would you like to do?\n").upper()

  # Removing Parenthesis for better readability and added index 0 of the word
  # that way it would work even if it has a typo.
  if user_choice[0] == 'D':

    # Variable to store deposit amount from user input
    deposit_amt = float(input('How much money would you like to deposit?'))
    print(f'Your new balance is {deposit(deposit_amt)}')

  # Return user balance
  elif user_choice[0] == 'B':
    balance()

  # If user selects W
  elif user_choice[0] == 'W':

    # Program ask the user for withdrawal amount
    withdrawal_amt = float(input('How much money would you like to withdrawal?'))

    # If the amount exceeds the user balance, the user will be prompt with the questions again
    if withdrawal_amt > account_balance:
      print('You do not have enough balance')

    # If the amount does not exceeds the balance return the value
    else:
      print(f'Your new balance is {withdrawal(withdrawal_amt)}')

  # If the user enter Q it will quit the program.
  elif user_choice[0] == 'Q':
    print('Thank you for using our ATM services, you are now exiting.\n')
    exiting = False
