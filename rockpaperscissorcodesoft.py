
import random

options = ["Rock", "Paper", "Scissors"]
user_choice = input("Select From The Following : Choose Rock, Paper ,Scissors: ")
computer_choice = random.choice(options)
print("Your Choice: ", user_choice)
print("Computers Choice: ", computer_choice)

 
if user_choice == computer_choice:

    print("Same Choice Hence It's A Tie!")

elif user_choice == "Rock" and computer_choice == "Scissors":

    print("You won!")

elif user_choice == "Paper" and computer_choice == "Rock":

    print("You won!")

elif user_choice == "Scissors" and computer_choice == "Paper":

    print("You Won!")

else:

    print("Computer Wins!")

print("If you Enjoyed then come back and challenge the computer again")   