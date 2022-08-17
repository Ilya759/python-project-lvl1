from prompt import string


RAUND_GAME = 3


def start(game):
    print('Welcome to the Brain Games!')
    name = string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.TEXT_GAME)
    cong = (f'Congratulations, {name}!')
    for _ in range(RAUND_GAME):
        question, correct_answer = game.question_and_answer()
        print(f'Question: {question}')
        user_answer = string("Your answer: ")
        finish = (f"'{user_answer}' is wrong answer ;(."
                  f"Correct answer was '{correct_answer}'.")
        if correct_answer != user_answer:
            print(finish)
            print(f"Let's try again, {name}!")
            break
        else:
            print('Correct!')
    else:
        print(cong)
