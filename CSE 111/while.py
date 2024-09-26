import random

def whileloopexample(number):
    rando = random.randint(100, 1000000)
    while number != rando:
        rando = random.randint(100, 1000000)
        print(rando)
    print(f'You guess the correct {number}')
print(whileloopexample(6109))