# Global Variables that holds the base charges for each category
budget_rate = 40
daily_rate = 60.00
weekly_rate = 190.00

# Ask the user to choose an option
rental_code = input("Please select one of the following options.\n (B)udget, (D)aily, or (W)eekly?\n").lower()
# Prompts the user to choose how many days or weeks
days_rented = int(input('For how many days would you like to rent the vehicle?\n'))
weeks_rented = int(input('For how many weeks would you like to rent the vehicle?\n'))

# Prompts the user to enter starting and ending odometer
odo_start = int(input("Enter starting Odometer"))
odo_end = int(input('Enter Ending Odometer'))

miles_driven = odo_end - odo_start

# Variable that controls the while loop
asking_user = True
# variable assigned to hold the total price
total_price = 0
while asking_user:

    # added index 0 for a more intuitive response to the user, will accept typos if the start with
    # the requested letter
    if rental_code[0] == 'b':
        # added miles charge to reflect the difference between the rental types
        miles_charge = miles_driven * .25
        # Total price plus miles charge
        total_price = (days_rented * budget_rate)+ miles_charge
        asking_user = False

    # Conditional for the second rental type
    elif rental_code[0] == 'd':
        # Gets the average daily miles driven

        average_daily_miles = miles_driven / days_rented
        # if miles driven are more than a 100 adds extra miles charge
        if average_daily_miles > 100:
            extra_miles = average_daily_miles - 100
            total_price = (days_rented * daily_rate)+ (extra_miles * .25)
            asking_user = False
        # if miles driven are 100 or less wont add extra miles
        else:
            total_price = days_rented * daily_rate
            asking_user = False

    elif rental_code[0] == 'w':
        # Gets the average weekly miles driven

        average_weekly_miles = miles_driven / weeks_rented
        # if miles driven are more than a 900 adds extra miles charge
        if average_weekly_miles > 900:
            miles_charge = 100
            total_price = (days_rented * weekly_rate) + miles_charge
            asking_user = False
        # if miles driven are 900 or less wont add extra miles
        else:
            total_price = weeks_rented * weekly_rate
            asking_user = False
    else:
        print('That is not an available option. we are continually working to add more options.')


# Customer Data
print(f'You selected the rental code {rental_code.upper()} and your total is {total_price}')
