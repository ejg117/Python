Account_names=[]
Account_balances=[]
Account_name = None
print('Enter the names and balances of bank accounts (type:quit when done)')
while Account_name != 'quit':
         Account_name= input('What is the name of this account? ')
         if Account_name != 'quit':
          Account_balance= float(input('What is the balance? '))

          Account_names.append(Account_name)
          Account_balances.append(Account_balance)
        
total=0
print('Account information:')
for i in range(len(Account_names)):
    print(f"{Account_names[i]} - ${Account_balances[i]}")

    total += Account_balances[i]
average = total / len(Account_balances)
print()
print(f"Total: ${total:.2f}")
print(f"Average: ${average:.2f}")