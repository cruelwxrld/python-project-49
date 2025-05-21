import random

import prompt

from brain_games import main as brain_games


def main(attempt=3):
    name = brain_games()
    print("Answer \"yes\" if the number is even, otherwise answer \"no\"")
    while attempt:
        question = random.randint(10, 100)
        print(f"Question: {question}")
        question = question % 2 == 0
        answer = prompt.string("Your answer: ").lower()
        answer_result = True if answer == "yes" else False
        if answer not in ("yes", "no"):
            answer_result = None
        answer_buffer = 'yes' if question else 'no'
        
        if question == answer_result:
            print("Correct!")
            attempt -= 1
        else:
            if answer_result:
                print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.")
            elif answer_result is None:
                print(f"'{answer}' is wrong answer ;(. Correct answer was '{answer_buffer}'.")
            else:
                print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.")
            print(f"Let's try again, {name}")
            break
    if attempt == 0:
        print(f'Congratulations, {name}!')
        
