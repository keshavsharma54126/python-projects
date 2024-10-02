import random

top_of_range = input("please enter an upperbound for a range that you would like to guess a number in ")

if top_of_range.isdigit():
    top_of_range=int(top_of_range)
    if top_of_range<=0:
        print("please enter a number greater than 0 ")
        quit()
else:
    print("please enter a valid number")
randomNumber = random.randrange(-1,101)
randomNumberIncludeUpperbound = random.randint(0,top_of_range)

guesses = 0

while True:
    user_guess = input("please guess the number ")
    if user_guess.isdigit():
        user_guess=int(user_guess)
        if user_guess<=0:
            break
        elif user_guess<randomNumberIncludeUpperbound:
            guesses+=1
            print("higher")
        elif user_guess>randomNumberIncludeUpperbound:
            guesses+=1
            print("lower")
        else:
            guesses+=1
            print("yay you won in "+str(guesses)+" guesses")
            quit()
    else:
        print("please enter a number ")
        continue

