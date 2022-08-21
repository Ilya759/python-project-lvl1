from prompt import string


ROUND_GAME = 3


def start(game):
    print('Welcome to the Brain Games!')
    name = string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.TEXT_GAME)
    congratulations = (f'Congratulations, {name}!')
    for _ in range(ROUND_GAME):
        question, correct_answer = game.play_mind_games()
        print(f'Question: {question}')
        user_answer = string("Your answer: ")
        if correct_answer != user_answer:
            print(f"""\"{user_answer}\" is wrong answer ;(.\
 Correct answer was \"{correct_answer}\".\nLet's try again, {name}!""")
            break
        else:
            print('Correct!')
    else:
        print(congratulations)
