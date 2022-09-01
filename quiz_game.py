print("welcome to my computer quiz!")

playing = input("do you want to play? ")

if playing.lower() != "yes":
    quit()
print("Okay! Let's play : ")
score = 0
answer = input("what does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('correct!')
    score += 1
else:
    print('incorrect!')

answer = input("what does PSU stands for? ")
if answer.lower() == "power suply":
    print('correct!')
    score += 1
else:
    print('incorrect!') 

answer = input("what does ROM  stand for? ")
if answer.lower() == "read only memory":
    print('correct!')
    score += 1
else:
    print('incorrect!')

answer = input("what does RAM stand for? ")
if answer == "random access memory":
    print('correct!')
    score += 1
else:
    print('incorrect!')
answer = input("what does GPU stands for? ")
if answer == "Graphics processing unit":
    print('correct!')
else:
    print('incorrect!')
print("you get " +str(score)+ "  answer correct!")
print(" you got " +str((score /4)* 100) + "%.")