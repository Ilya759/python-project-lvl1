from random import randint


TEXT_GAME = 'Answer "yes" if the number is even, otherwise answer "no".'
RANDOM_MIN_VALUE = 1
RANDOM_MAX_VALUE = 100


def play_mind_games():
    random_number = randint(RANDOM_MIN_VALUE, RANDOM_MAX_VALUE)
    if random_number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return random_number, correct_answer
