import prompt


def welcome_user():
    user = prompt.string('May I have your name? ')
    return user


def say_answer():
    answer = prompt.string("Your answer: ")
    return answer