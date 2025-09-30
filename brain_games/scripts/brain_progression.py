import random


def properties():
    random_pos = random.randint(1, 10)
    args = [str(var) for var in range(1, 10 * random_pos, random_pos)]
    take_random_pos = random.randint(0, len(args) - 1)
    answer_check = args[take_random_pos]
    question = " ".join(args).replace(answer_check, '..')
    return question, int(answer_check)


def main():
    from brain_games import engine, get_name
    print('Welcome to the Brain Games!')
    name = get_name()
    print(f'Hello, {name}!')
    print("What number is missing in the progression?")
    engine(name, "brain-progression")


