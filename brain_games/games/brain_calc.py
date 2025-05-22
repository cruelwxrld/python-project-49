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
    from brain_games import brain_main, engine
    name = brain_main()
    print("What is the result of the expression?")
    engine(name, "brain-calc")


