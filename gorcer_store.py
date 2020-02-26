# An empty dictionary and a grocery history list
grocery_item = {'name':'','number':'','price':''}
grocery_history = []

# Check variable to stop the loop if needed
# item_count to count items in the list
check = 'c'
item_count = 0

# while loop to ask the user for item name, quantity purchased and price per item.
while check == 'c':

    print("Item name:")
    grocery_item['name'] = input()

    print("Quantity Purchased:")
    grocery_item['number'] = input()

    print("Price Per Item:")
    grocery_item['price'] = input()
    grocery_history.append(grocery_item.copy())

    print("Would you like to enter another item?")

    # prompts user to continue or quit
    check = input( "Type 'c' for continue or 'q' to quit:")
    grand_total = 0.0
    item_count += 1

# for loop to print grocery list and add up item totals and calculate a grand total
for i in range(0, item_count):

  item_total = int(grocery_history[i]['number'])*float(grocery_history[i]['price'])
  grand_total += item_total

  print(f'{grocery_history[i]["number"]} {grocery_history[i]["name"]} @ ${grocery_history[i]["price"]}'
        f' ea = $ {item_total}')

#   prints grand total
print((f'Grand Total: $ {grand_total:.2f}'))


