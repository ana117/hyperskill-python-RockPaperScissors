import random

username = input("Enter your name: ")
print(f"Hello, {username}\n")

with open("rating.txt", "r") as reading:
    data = reading.readlines()

rating = 0
for line in data:
    if username in line:
        rating = int(line.split()[1])

rock = {"rock": "There is a draw (rock)",
        "paper": "Sorry, but the computer chose paper",
        "scissors": "Well done. The computer chose scissors and failed"}
rock_score = {"rock": 50,
              "paper": 0,
              "scissors": 100}

paper = {"rock": "Well done. The computer chose rock and failed",
         "paper": "There is a draw (paper)",
         "scissors": "Sorry, but the computer chose scissors"}
paper_score = {"rock": 100,
               "paper": 50,
               "scissors": 0}

scissors = {"rock": "Sorry, but the computer chose rock",
            "paper": "Well done. The computer chose paper and failed",
            "scissors": "There is a draw (scissors)"}
scissors_score = {"rock": 0,
                  "paper": 100,
                  "scissors": 50}

while True:
    user_input = input()
    if user_input == "!exit":
        print("Bye!")
        break
    elif user_input == "!rating":
        print(f"Your rating: {rating}")
    else:
        choice_list = ["scissors", "rock", "paper"]
        computer = choice_list[random.randint(0, 2)]

        if user_input == "rock":
            print(rock[computer])
            rating += rock_score[computer]

        elif user_input == "paper":
            print(paper[computer])
            rating += paper_score[computer]

        elif user_input == "scissors":
            print(scissors[computer])
            rating += scissors_score[computer]

        else:
            print("Invalid input")