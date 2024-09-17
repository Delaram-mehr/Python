
"""
Word Guessing Game

A simple Python game where the player has to guess a randomly selected name from a predefined list.

- The game picks a random name and displays it as a series of hyphens for unguessed letters.
- The player inputs guesses one character at a time.
- The game provides feedback on correct and incorrect guesses.
- The player wins if they guess all letters correctly before running out of guesses.
- The game ends when the player either wins or exhausts all guesses.

"""

import random

# List of names to choose from
names = ['Hasan', 'Ali', 'Behnam', 'Mahmoud', 'Vahid', 'Amin', 'Maryam', 'Zahra']

# Returns a random lowercase name from the list.
def get_random_name(names):
    return random.choice(names).lower()

# Shows the current guessed state with hyphens.
def display_current_guess(guessed_list):
    return "-".join(guessed_list)

# Updates guessed_list based on the user's guess.
def process_guess(selected_name, guessed_list, guessed_char):
    correct_guess = False
    for idx, char in enumerate(selected_name):
        if char == guessed_char:
            guessed_list[idx] = guessed_char
            correct_guess = True
    return correct_guess

# Runs the game.
def run_game(names):
    selected_name = get_random_name(names)
    guess_count = len(selected_name)
    guessed_list = ['-'] * len(selected_name)
    print(display_current_guess(guessed_list))

    while guess_count > 0:
        guessed_char = input('Enter a character: \n').lower()

        if guessed_char.isalpha() and len(guessed_char) == 1:
            if guessed_char in selected_name:
                if guessed_char in guessed_list:
                    print("Character already guessed. Try a new one.")
                else:
                    if process_guess(selected_name, guessed_list, guessed_char):
                        print(f"Perfect => {display_current_guess(guessed_list)}")
                        if '-' not in guessed_list:
                            print("You won!")
                            break
                    else:
                        print("Error processing the guess.")
            else:
                guess_count -= 1
                print(f"Wrong! Remaining guesses: {guess_count}")
        else:
            print("Enter a valid single character.")
    
    if guess_count == 0:
        print(f"Game Over! The word was '{selected_name}'.")

if __name__ == "__main__":
    run_game(names)
