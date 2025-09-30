import random


def properties():
    arg1, arg2 = random.randint(1, 100), random.randint(1, 100)
    operator = random.choice(["+", "-", "*"])
    match operator:
        case "+":
            answer_check = arg1 + arg2
        case "-":
            answer_check = arg1 - arg2
        case "*":
            answer_check = arg1 * arg2
    question = f"{arg1} {operator} {arg2}"
    return question, answer_check


def main():
    from brain_games import engine, get_name
    print('Welcome to the Brain Games!')
    name = get_name()
    print(f'Hello, {name}!')
    print("What is the result of the expression?")
    engine(name, "brain-calc")
