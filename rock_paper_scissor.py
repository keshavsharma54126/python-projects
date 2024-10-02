import random

options = ["rock","paper","scissor"]
user_wins=0
computer_wins=0

while True:
    user_input = input("please type Rock,Paper,Scissor to play or Q to quit ").lower()
    if user_input=="q":
        break;

    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    print("you chose "+user_input+" and the computer chose "+options[random_number])

    if user_input=="rock" and options[random_number]=="scissor":
        print("you won")
        user_wins+=1
    elif user_input=="paper" and options[random_number]=="rock":
        print("you won")
        user_wins+=1
    elif user_input=="scissor" and options[random_number]=="paper":
        print("you won")
        user_wins+=1

    else:
        print("computer won")
        computer_wins+=1

print("you won ",user_wins," number of times")
print("computer won ",computer_wins," number of times")
print("Good bye")       