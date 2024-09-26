# favletter = input('What is your favorite letter?')
# word="commitment"
# for letter in word: 
#  if letter.lower() == favletter.lower():
#   print (letter.replace(favletter, '_'), end="")
#  else:
#   print (letter.lower(), end="")

s="In coming days, it will not be possible to survive spiritually without the \
 guiding, directing, comforting, and constant influence of the Holy Ghost."
n = int(input('Pick a number '))
for i, letter in enumerate(s): 
 if i % n == 0:
    print(letter.upper(), end="")
else:
     print(letter.lower(), end="")
