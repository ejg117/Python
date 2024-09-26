# def Compute_tithing(amount):
#     tithe = amount * 0.08
#     return tithe

# def format_tithing(tithe):
#     return f"${tithe:,.2f}"

# def computer_and_format_tithe(amount):
#     t = Compute_tithing(amount)
#     return f"${t:,.2f}"

# dollar_amount = input('What is the amount to be tithed? $')

# tithing = computer_and_format_tithe(float(dollar_amount))

def ask_yes_no(prompt, affirmative = 'Y', negative = "N"):
    prompt = f''
    answer = input(f"{prompt} ({affirmative.upper()}/{negative.upper()}) ".lower())
    while answer not in ['y', 'n']:
        if answer == affirmative.lower():
            return True
        elif answer == negative.lower():
            return False
        else:
            print(f"Invalid input: please enter {affirmative.lower()} or {negative.lower()}." )
            answer = input(prompt).lower()

is_raining = ask_yes_no('Is it raining outside? ')
temp = float(input('What is the temperature outside? '))
is_windy = ask_yes_no('Is it windy?', affirmative="Yessir", negative="Nope")
should_run = False
do_run = "You should go running"
do_not_run = "Don't do it!"


