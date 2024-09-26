print('Welcome to the word guessing game!')
word = "clairvoyance"
c = 0
hint = "_ " * len(word)
print(f'Your hint is {hint}')

correctly_guessed = set()

while True:
    userguess = input("What is your guess? ").lower()
    c += 1

    if userguess == word.lower():
        break

    if len(userguess) == 1 and userguess.isalpha():
        if userguess in correctly_guessed:
            print(f'You already guessed the letter {userguess.upper()}.')
        else:
            correctly_guessed.add(userguess)
            hint = ""
            for letter in word:
                if letter in correctly_guessed:
                    hint += letter.upper() + ' '
                else:
                    hint += '_ '
            print(f'Your hint is {hint.strip()}')

            if all(letter in correctly_guessed for letter in word):
                break

    elif len(userguess) == len(word) and userguess.isalpha():
        new_hint = ""
        for i, (user_char, word_char) in enumerate(zip(userguess, word)):
            if user_char == word_char:
                new_hint += user_char.upper() + ' '
            else:
                new_hint += user_char.lower() + ' '
        hint = new_hint.strip()
        print(f'Your hint is {hint}')
        
        if hint.replace(" ", "") == word:
            print(f'Congrats you guessed the word {word.capitalize()} in {c} tries!')
            break
        elif all(letter in correctly_guessed for letter in word):
            print(f'Congrats you guessed the word {word.capitalize()} in {c} tries!')
            break
    else:
        print('Please enter a valid letter or word.')
print(f'Congrats you guessed the word {word.capitalize()} in {c} guesses!')
