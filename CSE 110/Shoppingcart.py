print("\033[38;5;201m")
print('Welcome to the shopping Cart program!')
selection=0
Items= []
Compute_Totals= []
Items_in_cart= []
#Display the menu
menu=[
    '1. Add Item', 
    '2. View cart', 
    '3. Remove item', 
    '4. Compute Total', 
    '5. Quit'
]
c=0
while selection != 5:
    print('')
    print('Please select one of the following:')
    for action in menu:
        print(action)
    selection= int(input('Please enter an action: '))
    if selection == 1:
        for Item in Items:
             print(f'-{Item}')
        Item_Selection= input('What item would you like to add? ')
        Compute_Total= float(input('What is the price of the item? '))
        Items_in_cart.append(Item_Selection)
        Compute_Totals.append(Compute_Total)
        for i in Items_in_cart:
         print(f"'{i}' has been added to the cart.")
    elif selection == 2:
        print('The contents of the shopping cart are:')
        for i in range(len(Items_in_cart)):
         print (f"{i + 1}. {Items_in_cart[i]} - ${Compute_Totals[i]: .2f}")
    elif selection == 3:
         remove_item= input('What item would you like to remove? ')
         if remove_item in Items_in_cart:
              idx_to_rmv= Items_in_cart.index(remove_item)
              Items_in_cart.pop(idx_to_rmv)
              Compute_Totals.pop(idx_to_rmv)
              print('Item removed') 
         else:
              print('Item not found in cart.')
    elif selection == 4:
        total=0
        for price in Compute_Totals:
         total += price
        print(f'The Total price of items in the shopping cart is ${total:.2f}')
    else:
        print('Invalid input (bruh)')
print('Thank you, Goodbye.')
