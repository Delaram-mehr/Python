
"""
Math Quiz Game

This Python script generates random math questions involving addition, subtraction, multiplication, and division.
Players have a limited time to answer each question, and the game continues until a set number of questions is reached.
Scores are updated based on correct answers, and the final score is displayed at the end.
"""

import random
import time

def generate_question():
    
    # Generate two random numbers
    a = random.randint(1, 9)
    b = random.randint(1, 9)

    # Select a random operator
    operators = ['+', '-', '*', '/']
    operator = random.choice(operators)

    # Format the question
    question = f"{a} {operator} {b} = ?"

    # Calculate the answer based on the operator
    if operator == '+':
        answer = a + b
    elif operator == '-':
        answer = a - b
    elif operator == '*':
        answer = a * b
    else:
        answer = round(a / b, 2)  # Rounded to 2 decimal places

    return question, answer

# Main function to run the math quiz game.
def main():
    
    max_questions = 5
    score = 0
    time_limit = 10

    for _ in range(max_questions):
        question, correct_answer = generate_question()
        print(question)

        start_time = time.time()
        user_input = input("Enter your answer: ")

        # Calculate the time taken
        elapsed_time = time.time() - start_time

        if elapsed_time < time_limit:
            try:
                user_answer = float(user_input)
                if user_answer == correct_answer:
                    score += 1
                    print(f"Correct! Your score: {score}")
                else:
                    print(f"Wrong! The correct answer was: {correct_answer}")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        else:
            print("Time's up!")

    print(f"FINAL SCORE: {score} out of {max_questions}")

if __name__ == "__main__":
    main()
