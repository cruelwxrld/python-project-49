import random


def properties():
    question = random.randint(1, 100)
    answer_check = "yes" if question % 2 == 0 else 'no'
    return question, answer_check


def main():
    from brain_games import brain_main, engine, get_name
    print('Welcome to the Brain Games!')
    name = get_name()
    print(f'Hello, {name}!')
    print("Answer \"yes\" if the number is even, otherwise answer \"no\"")
    engine(name, "brain-even")


