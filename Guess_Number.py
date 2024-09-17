
"""
Number Guessing Game

This is a simple number guessing game where the user has 5 attempts to guess a randomly generated number within a specified range.

How to Play:
1. The game will ask you to enter the lower and upper bounds for the range.
2. After that, you will have 5 guesses to identify the number.
3. After each guess, the game will tell you whether your guess is higher or lower than the target number.
4. If you guess correctly, the game will congratulate you. Otherwise, it will reveal the correct number after all attempts are used.

"""

import random

# Get user input and ensure it is a valid integer.
def get_user_input(prompt): 

    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


# Generate a random number within the given range.
def generate_random_number(low, high): 

    return random.randint(low, high)


# Prompt the user for their guess and return it as an integer.
def get_user_guess(guess_count): 

    return get_user_input(f"Remaining guesses: {guess_count} => Enter your next guess: \n")


# Main game logic where the user tries to guess the number.
def play_game(low, high): 

    target_number = generate_random_number(low, high)
    guess_count = 5

    while guess_count > 0:
        user_guess = get_user_guess(guess_count)

        if user_guess == target_number:
            print("Great! Your guess is correct!")
            break
        elif user_guess < target_number:
            print("Your guess is lower than the selected number.")
        else:
            print("Your guess is higher than the selected number.")

        guess_count -= 1

    if guess_count == 0:
        print(f"Sorry, you've run out of guesses. The correct number was {target_number}.")


# Run the number guessing game with user-defined bounds.
def main(): 

    print("Welcome to the Number Guessing Game!")

    low = get_user_input('Enter lower bound: \n')
    high = get_user_input('Enter upper bound: \n')

    if low >= high:
        print("Invalid range. Lower bound must be less than upper bound.")
    else:
        play_game(low, high)

if __name__ == "__main__":
    main()
