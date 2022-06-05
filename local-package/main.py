import random

def theResult(a,b):
    if(a=="S"):
        a="Scissor"
    elif(a=="P"):
        a="Paper"
    else:
        a="Rock"
    
    if(b=="S"):
        b="Scissor"
    elif(b=="P"):
        b="Paper"
    else:
        b="Rock"
    
    print("Player - "+a+" vs CPU - "+b)


play=True
while(play):
    print("Welcome to our Rock, Paper and Scissor Game")
    print("Usage: Input the letter P for Paper, R for Rock or S for Scissor, Good Luck!")
    userChoice=input("Please, Introduce your choice:[P,R or S]:")

    if userChoice == "S" or userChoice == "R" or userChoice == "P":
        #print("OK")
        myChoices=["R","P","S"]
        pcChoice=random.choice(myChoices)

        if pcChoice == userChoice:
            print("It's a Tie, Try again!")
        else:
            if (userChoice=="P" and pcChoice=="R") or (userChoice=="S" and pcChoice=="R") or (userChoice=="P" and pcChoice=="S"):
                print("The PC is the winner!")
                theResult(userChoice,pcChoice)
                play=False
            elif (userChoice=="R" and pcChoice=="P") or (userChoice=="R" and pcChoice=="S") or (userChoice=="S" and pcChoice=="P"):
                print("You are the winner!")
                theResult(userChoice,pcChoice)
                play=False
            else:
                print("Something is wrong!!!")

    else:
        print("Wrong entry, please Try again!")