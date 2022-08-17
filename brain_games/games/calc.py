from random import randint
from random import choice


TEXT_GAME = 'What is the result of the expression?'
RANDOM_MIN_VALUE = 1
RANDOM_MAX_VALUE = 100


def question_and_answer():
    operators = ['+', '-', '*']
    number1 = randint(RANDOM_MIN_VALUE, RANDOM_MAX_VALUE)
    number2 = randint(RANDOM_MIN_VALUE, RANDOM_MAX_VALUE)
    random_operator = choice(operators)
    if random_operator == '+':
        correct_answer = number1 + number2
    elif random_operator == '-':
        correct_answer = number1 - number2
    elif random_operator == '*':
        correct_answer = number1 * number2
    question = f'{number1} {random_operator} {number2}'
    return question, str(correct_answer)
