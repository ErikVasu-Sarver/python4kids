import random


computers_number = random.randint(1,100)
prompt = 'what is your guess? '
while True:
    players_guess = raw_input(prompt)
    if computers_number == int(players_guess):
        print ('Correct!')
        break
    elif computers_number > int(players_guess):
        print ('Too Low')
    else:
        print ('Too High')
