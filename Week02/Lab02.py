# Solution for the Week 02 Lab
import random

choices = ["Rock", "Paper", "Scissors"]

playerChoice = input("Enter a number between 1 to 3 for the following choices:\n1-Rock \n2-Paper \n3-Scissors \n\n")

playerChoice = int(playerChoice)

if playerChoice < 1 or playerChoice > 3:
    print("Error: Choice should be between 1 and 3!")
else:
    computerChoice = random.randint(1,3)

    if playerChoice == computerChoice:
        print("Tie")
    elif playerChoice == 1 and computerChoice == 3:
        print("Rock beats Scissors - You Win!")
    elif playerChoice == 2 and computerChoice == 1:
        print("Paper beats Rocks - You Win!")
    elif playerChoice == 3 and computerChoice == 2:
        print("Scissors beats Paper - You Win!")
    else:
        print("You lose! :c ")