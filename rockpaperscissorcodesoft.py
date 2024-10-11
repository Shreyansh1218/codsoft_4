
import random

while(True):
    options = ["Rock", "Paper", "Scissors"]
    user_choice = input("Select From The Following : Choose Rock, Paper ,Scissors: ")
    computer_choice = random.choice(options)
    print("Your Choice: ", user_choice)
    print("Computers Choice: ", computer_choice)

 
    if user_choice == computer_choice:

        print("Same Choice Hence It's A Tie!")
        answer=input("Want To Play Again then type yes else type no:- ")
        if answer=="no" :
            break
        else:
            continue    

    elif user_choice == "Rock" and computer_choice == "Scissors":

        print("You won!")
        answer=input("Want To Play Again :- ")
        if answer=="no":
            break
        else:
            continue

    elif user_choice == "Paper" and computer_choice == "Rock":

        print("You won!")
        answer=input("Want To Play Again :- ")
        if answer=="no":
            break
        else:
            continue

 
    elif user_choice == "Scissors" and computer_choice == "Paper":

        print("You Won!")
        answer=input("Want To Play Again :- ")
        if answer=="no":
            break
        else:
            continue


    else:

        print("Computer Wins!")
        answer=input("Want To Play Again :- ")
        if answer=="no":
           break
        else:
           continue

print("THANKYOU")   




   




