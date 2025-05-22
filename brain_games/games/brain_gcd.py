import random


def properties():
    arg1, arg2 = random.randint(1, 100), random.randint(1, 100)
    ranged = range(min(arg1, arg2), 0, -1)
    nod = filter(lambda x: arg1 % x == 0 and arg2 % x == 0, ranged)
    answer_check = max(list(nod))
    question = f'{arg1} {arg2}'
    return question, answer_check


def main():
    from brain_games import brain_main, engine
    name = brain_main()
    print("Find the greatest common divisor of given numbers.")
    engine(name, "brain-gcd")


