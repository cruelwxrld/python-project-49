from brain_games import welcome_user


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print(f'Hello, {name}!')
    return name