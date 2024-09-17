"""
Rock, Paper, Scissors Game

Overview :

This is a simple implementation of the classic game "Rock, Paper, Scissors" in Python.
The game allows a user to play against the computer, and it continues until one side reaches 3 points.
The user is prompted to re-enter their choice if the choices of the user and the computer are the same, and the game displays the ongoing scores until a winner is determined.

Features :

1. User input for choosing rock, paper, or scissors.
2. Computer makes a random choice.
3. The game continues until one player scores 3 points.
4. Handles invalid user input by prompting again.
5. Displays the current scores after each round.
"""

import random

# Step 1
options = ["R", "P", "S"]

# Initialize scores
user_score = 0
pc_score = 0

while user_score < 3 and pc_score < 3:
    # Step 2
    user_choice = input(f"Please select your option from the list of {options} \n").upper()

    # Check if the user's choice is valid
    if user_choice not in options:
        print("Invalid choice. Please select R, P, or S.")
        continue  # Ask for input again if the choice is invalid

    # Step 3: Computer's choice is random
    pc_choice = random.choice(options)
    print(f"PC choice is {pc_choice}")

    # Step 4: Comparison and determining the winner
    if user_choice == pc_choice:
        print("It's a tie! Try again!")
    else:
        if user_choice == "R":
            if pc_choice == "P":
                print("PC wins this round!")
                pc_score += 1  # Increment PC's score if PC wins
            else:
                print("User wins this round!")
                user_score += 1  # Increment User's score if User wins

        elif user_choice == "P":
            if pc_choice == "S":
                print("PC wins this round!")
                pc_score += 1  
            else:
                print("User wins this round!")
                user_score += 1  

        elif user_choice == "S":
            if pc_choice == "R":
                print("PC wins this round!")
                pc_score += 1  
            else:
                print("User wins this round!")
                user_score += 1  

    # Display current scores
    print(f"Scores -> User: {user_score}, PC: {pc_score}")

# Determine the overall winner
if user_score == 3:
    print("User is the overall winner!")
else:
    print("PC is the overall winner!")

    




