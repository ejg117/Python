from statistics import mean
print('Enter a list of numbers, type 0 when finished.')
numbers=[]
number=1
while number != 0:
    number=int(input('Enter number: '))
    if number !=0:
       numbers.append(number)        
s=sum(numbers)
print(f'The sum is: {s} ')
a= mean(numbers)
print(f'The average is: {a}')
L= max(numbers)
print(f'The largest number is: {L}')
m= min(numbers)
print(f'The smallest number is: {m}')
numbers.sort()
print('The sorted list is:')
for i in numbers:
    print(i)