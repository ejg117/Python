import random
question = random.randint(1, 10)
question2= int(input("What is your guess? "))
n=1

while True:
 if question < question2:
    print('Lower')
    question2= int(input("What is your guess? "))
    n+1
 if question > question2:
    print ('Higher')
    question2= int(input("What is your guess? "))
    n+1
 elif question == question2:
    print('You guessed it!')
    print(f'It took you {n} guesses! ')
    again=str(input("Play again? "))
       