print("welcome to my computer quiz")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("okay!let's play: ")

score =0

answer = input("what does CPU stand for? ")
if answer == "central processing unit":
    score+=1
    print("correct answer!"+ "score="+ str(score))

elif answer == "Central Processing Unit":
    print("correct answer")
else:
    print("incorrect answer")

answer = input("what does GPU stand for? ")
if answer == "graphical processing unit":
    score+=1
    print("correct answer!"+ "score="+ str(score))
elif answer == "Graphical Processing Unit":
    print("correct answer")
else:
    print("incorrect answer")

print("final socre = "+str(score) + " you got "+str((score)/2 *100)+"%")
print("yay you answered everything correctly")