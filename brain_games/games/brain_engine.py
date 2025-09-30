def run_game(question, check, attempt, name):
    from brain_games import say_answer
    print(f"Question: {question}")
    answer = say_answer()

    try:
        answer = int(answer)
    except ValueError:
        answer = answer.lower()
    
    if check == answer:
        print("Correct!")
        return attempt - 1
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{check}'")
        print(f"Let's try again, {name}!")
        return -1


def engine(name, type_of_game):
    match type_of_game:
        case "brain-even":
            from brain_games import properties_even
            properties = properties_even
        case "brain-calc":
            from brain_games import properties_calc
            properties = properties_calc
        case "brain-gcd":
            from brain_games import properties_gcd
            properties = properties_gcd
        case "brain-progression":
            from brain_games import properties_progression
            properties = properties_progression
        case "brain-prime":
            from brain_games import properties_prime
            properties = properties_prime

    def wrapped(attempt=3):
        if attempt == 0:
            print(f"Congratulations, {name}!")
            return
        question, answer_check = properties()
        remaining = run_game(question, answer_check, attempt, name)
        if remaining >= 0:
            wrapped(remaining)
    wrapped()
