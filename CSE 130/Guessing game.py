import random
#1. Name: 
#Ephraim Gunnell

#2. Assignment Name: 
# Lab 01: Guessing Game

#3. Assignment Description:
# - Prompt the user for how difficult the game will be. Ask for an integer.
# - Generate a random number between 1 and a chosen value
# - Give the user instructions as to what he or she will be doing
# - Intialize the sentinal and the array of guesses
# - Play the guessing game.
# - Prompt the user for a number
# - Store the number in an array so it can be displayed later.
# - Make a decision: was the guess too high, too low, or just right.
# - Give the user a report: How many guesses and what the guesses were.

#4. What was the hardest part? Be as specific as possible.

#The hardest part about this assignment was remembering the Python I learned in the past. Some of the Python was pretty 
#simple such as print statements, if elif and else statements, and variables. I started having a harder time when it came to
#specifically loops and lists not because I didn't know what they were but because I had a hard time integrating them in this
#assignment. When I was trying to figure out why the counter for the numbers listed it was because I was using math to add
#the guessed numbers to the list. I had a more harder time remembering the commands associated with loops and lists and
#what each command did. Thankfully I had plenty of resources to figure out what they did from Cse 110 before and Cse 111
#which I am currently taking on top of this class. So if anything I need more hands-on practice to know and use the specific commands.

#5.

#3 to 4 hours to complete the assignment 
def guessing_game():
    print('This is the "guess a number" game.')
    print('You try to guess a random number in the smallest number of attempts.')
    dif_lvl = int(input('Pick a positive integer: '))
    tries = 0
    guessed_numbers = []
    guesser = random.randint(1,dif_lvl)
    while True:
        Response= int(input(f'Guess a number between 1 and {dif_lvl} '))
        tries+=1
        guessed_numbers.append(Response)

        if Response < guesser:
            print('     Too low!')
            print(Response)
        elif Response > guesser:
            print('     Too High!')
            print(Response)
        else:
            print(f'You guessed the number in {tries} guesses') 
            print(f'the numbers you guessed were {guessed_numbers}')
            break
guessing_game()