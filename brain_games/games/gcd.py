from random import randint
from math import gcd


TEXT_GAME = 'Find the greatest common divisor of given numbers.'
RANDOM_MIN_VALUE = 1
RANDOM_MAX_VALUE = 100


def question_and_answer():
    number1 = randint(RANDOM_MIN_VALUE, RANDOM_MAX_VALUE)
    number2 = randint(RANDOM_MIN_VALUE, RANDOM_MAX_VALUE)
    question = (f'{number1} {number2}')
    correct_answer = str(gcd(number1, number2))
    return question, correct_answer
