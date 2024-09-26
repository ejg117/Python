# word="longestword"

# for letter in word:
#     print(letter)

# for i in range(len(word)):
#  letter = word[i]
#  print(letter)

# print()
# movies = [
#     'Batman Begins', 
#     'Hulk'
#     ]

# movies.append("Dune")

#print(movies)
# for movie in movies:
#     print(f'\t-{movie}')

# Fast food menu
order = []
order_qty = []
selection= 0
drinks = ['Water', 'Root Beer', 'Guarana']
emtrees = ['Burger',  ]
menu=[
    'Drink',
    'Entree',
    'Side', 
    'Sauces', 
    ]
menu.append('Dessert')
menu.append('Order Complete')

#Display the menu
print('What would you like to order?')

while selection != len(menu) - 1:
    for i in range(len(menu)):
        action = menu[i]
        print(f'{i + 1} - {action}')
    selection= int(input(f'Enter 1-{len(menu)}: ')) - 1

    # If ordering drinks
    if selection == 0:
        print('Drinks available are:')
        for drink in drinks:
          print(f'-{drink.title()}')
        drink_selection= input('Which drink would you like? ')
        order.append(drink_selection) 
        qty = int(input('How many would you like to order? '))
        order_qty.append(qty)
    print()
    print(f'You ordered: ')
    for i in range(len(order)):
        item = order[i]
        qty = order_qty[i]
        print(f'-{item.title()} ({qty})')