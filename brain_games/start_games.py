from prompt import string


roundsCount = 3


def start(game):
    print('Welcome to the Brain Games!')
    name = string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.TEXT_GAME)
    for _ in range(roundsCount):
        question, correct_answer = game.generate_data_for_the_game()
        print(f'Question: {question}')
        user_answer = string('Your answer: ')
        if correct_answer != user_answer:
            print(f'\'{user_answer}\' is wrong answer ;(. '
                  f'Correct answer was \'{correct_answer}\'')
            print(f'Let\'s try again, {name}!')
            break
        else:
            print('Correct!')
    else:
        print(f'Congratulations, {name}!')
