import random

username = input("Enter your name: ")
print(f"Hello, {username}")

with open("rating.txt", "r") as file_name:
    data = file_name.readlines()

rating = 0
for line in data:
    if username in line:
        rating = int(line.split()[1])

rules = input()
if rules.strip() == "":
    rules = "rock,paper,scissors"
print("Okay, let's start")

winning_cases = {
    'water': ['snake', 'human', 'tree', 'wolf', 'sponge', 'paper', 'air'],
    'dragon': ['human', 'tree', 'wolf', 'sponge', 'paper', 'air', 'water'],
    'devil': ['tree', 'wolf', 'sponge', 'paper', 'air', 'water', 'dragon'],
    'lightning': ['wolf', 'sponge', 'paper', 'air', 'water', 'dragon', 'devil'],
    'gun': ['sponge', 'paper', 'air', 'water', 'dragon', 'devil', 'lightning'],
    'rock': ['paper', 'air', 'water', 'dragon', 'devil', 'lightning', 'gun'],
    'fire': ['air', 'water', 'dragon', 'devil', 'lightning', 'gun', 'rock'],
    'scissors': ['water', 'dragon', 'devil', 'lightning', 'gun', 'rock', 'fire'],
    'snake': ['dragon', 'devil', 'lightning', 'gun', 'rock', 'fire', 'scissors'],
    'human': ['devil', 'lightning', 'gun', 'rock', 'fire', 'scissors', 'snake'],
    'tree': ['lightning', 'gun', 'rock', 'fire', 'scissors', 'snake', 'human'],
    'wolf': ['gun', 'rock', 'fire', 'scissors', 'snake', 'human', 'tree'],
    'sponge': ['rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf'],
    'paper': ['rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'sponge'],
    'air': ['fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'sponge', 'paper']
}

losing_cases = {
    'water': ['scissors', 'fire', 'rock', 'hun', 'lightning', 'devil', 'dragon'],
    'dragon': ['snake', 'scissors', 'fire', 'rock', 'gun', 'lightning', 'devil'],
    'devil': ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun'],
    'gun': ['wolf', 'tree', 'human', 'snake', 'scissors', 'fire', 'rock'],
    'rock': ['sponge', 'wolf', 'tree', 'human', 'snake', 'scissors', 'fire'],
    'fire': ['paper', 'sponge', 'wolf', 'tree', 'human', 'snake', 'scissors'],
    'scissors': ['air', 'paper', 'sponge', 'wolf', 'tree', 'human', 'snake'],
    'snake': ['water', 'air', 'paper', 'sponge', 'wolf', 'tree', 'human'],
    'human': ['dragon', 'water', 'air', 'paper', 'sponge', 'wolf', 'tree'],
    'tree': ['devil', 'dragon', 'water', 'air', 'paper', 'sponge', 'wolf'],
    'wolf': ['lightning', 'devil', 'dragon', 'water', 'air', 'paper', 'sponge'],
    'sponge': ['gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper'],
    'paper': ['rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air'],
    'air': ['fire', 'rock', 'gun', 'lightning', 'devil', 'dragon', 'water'],
    'lightning': ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun']
}

choices = rules.split(",")

while True:
    user_input = input()
    if user_input == "!exit":
        print("Bye!")
        break
    elif user_input == "!rating":
        print(f"Your rating: {rating}")
    elif user_input in choices:
        lose = [i for i in winning_cases[user_input] if i in choices]
        win = [i for i in losing_cases[user_input] if i in choices]
        computer = choices[random.randint(0, len(choices)-1)]

        if computer in win:
            condition = "win"
        elif computer in lose:
            condition = "lose"
        else:
            condition = "draw"

        if condition == "win":
            print(f"Well done. The computer chose {computer} and failed")
            rating += 100
        elif condition == "lose":
            print(f"Sorry, but the computer chose {computer}")
        elif condition == "draw":
            print(f"There is a draw ({computer})")
            rating += 50

    else:
        print("Invalid input")