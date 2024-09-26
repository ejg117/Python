def budget(mandatory, tax = .06, savings = .25, spending = .49, tithing = .1):
   print (f'Tax amount: {mandatory * tax: .2f}')
   print (f'Savings amount: {mandatory * savings: .2f}')
   print (f'Spending amount: {mandatory * spending: .2f}')
   print (f'Tithing amount: {mandatory * tithing: .2f}')
   print (mandatory)
budget(60000)
