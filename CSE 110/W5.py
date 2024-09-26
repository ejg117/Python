do_it = input('Should I do it?').lower()

if do_it == 'yes':
    print("I did it!")
elif do_it == 'no' :
   print("I didn't do it.")
elif do_it == 'probably'
    print('I might have done')
else: 
    print("I didn't know what to do?")
if do_it.upper() == 'YES':
    print("redudant example, but yes, I did it again.")

is_raining = input('Is it raining outside? ').lower()
temp = float(input('What is the temperature outside? '))

if is_raining == 'yes':
    if temp > 60:
        print("nah just go outside and run")
    else: 
        print ("Dont' do it")
elif is_raining == 'no' :
   if temp > 90:
        print("For your safety do it")
    else:
        print ("You should probably go running... sorryu")
