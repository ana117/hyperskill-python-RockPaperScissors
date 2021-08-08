import random

win = {'rock': 'Well done. Computer chose scissors and failed',
        'paper': 'Well done. Computer chose rock and failed',
        'scissors': 'Well done. Computer chose paper and failed'}

draw = {'rock': 'There is a draw (rock)',
        'paper': 'There is a draw (paper)',
        'scissors': 'There is a draw (scissors)'}
    
lose = {'rock': 'Sorry, but computer chose paper',
        'paper': 'Sorry, but computer chose scissors',
        'scissors': 'Sorry, but computer chose rock'}
        

while True:
        user = input()
        if user in ['rock', 'paper', 'scissors']:
                randomizer = random.choice('123')
                if randomizer == '1':
                        print(win[user])
                elif randomizer == '2':
                        print(draw[user])
                elif randomizer == '3':
                        print(lose[user])
        elif user == "!exit":
                print("Bye!")
                break
        else:
                print("Invalid input")