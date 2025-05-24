import random


def properties():
    answer = random.randint(1, 100)
    is_prime = True
    if answer < 2:
        is_prime = False
    else:
        for num in range(2, int(answer ** 0.5) + 1):
            if answer % num == 0:
                is_prime = False
                break
    answer_check = "yes" if is_prime else "no"
    return answer, answer_check


def main():
    from brain_games import brain_main, engine
    name = brain_main()
    print("Answer \"yes\" if given number is prime. Otherwise answer \"no\".")
    engine(name, "brain-prime")


