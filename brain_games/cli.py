import prompt # type: ignore

def welcome_user():
    user = prompt.string('May I have your name? ')
    return user