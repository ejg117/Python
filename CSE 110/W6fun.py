# answer = input('Should I do it?')
# answer_bool = answer.lower() == 'yes'
# answer_bool = True

# answer_bool = answer.lower() == 'yes'
# if answer_bool == 'yes':
#     print('I did it')

# is_raining = input('Is it raining outside? ').lower()
# temp = float(input('What is the temperature outside? '))
# is_windy = input ('Is it windy?').lower()
# should_run = False
# do_run = "You should go running"
# do_not_run = "Don't do it!"

# if is_raining and is_windy == 'yes':
#     should_run = False
# elif is_raining and temp > 60:
#     should_run = True
# elif is_raining:
#         print("Don't do it!!")
# elif not is_raining:
#    if temp > 90:
#         print("For your safety don't do it")
#    if temp < 38:
#     else:
#         print ("You should probably go running... sorryu")

# is_raining = input('Is it raining outside? ').lower()
# temp = float(input('What is the temperature outside? '))
# is_windy = input ('Is it windy?').lower()

# if is_raining == 'yes' and is_windy == 'no' or temp > 80:
#     print('Go running')
# else:
#     print("Don't do it")
vowels = "aeiou"
noun = input('Choose an noun: ')
article = 'a'

if noun[0] in vowels:
    article = 'an'
else:
    article = 'a'

print(f'I would like to give you {article} {noun}')



# print(f'I would like to give you an {noun}') 