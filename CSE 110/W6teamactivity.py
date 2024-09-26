rider1 = int(input("What is the age of the first rider? "))
rider1h = float(input("What is the height of the first rider? "))
riderpossible2 = input('Is there a second rider (yes/no)? ')

if riderpossible2.lower() == 'no':
    if rider1 >= 18 and rider1h >= 62:
        print('Welcome to the ride. Please be safe and have fun!')
    else:
        print('Sorry, you may not ride.')
elif riderpossible2.lower() == 'yes':
    rider2 = int(input("What is the age of the second rider? "))
    rider2h = float(input("What is the height of the second rider? "))
    
    if (rider1 >= 18 and rider1h >= 62) or (rider2 >= 18 and rider2h >= 36):
        print('Welcome to the ride. Please be safe and have fun!')
    else:
        print('Sorry, you may not ride.')
else:
  print('Sorry, you may not ride.')