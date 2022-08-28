from random import randint


TEXT_GAME = 'What number is missing in the progression?'
MINIMUM_PROG_START = 1
MAXIMUM_PROG_START = 10
MINIMUM_PROG_STEP = 2
MAXIMUM_PROG_STEP = 5
MINIMUM_PROG_LENGTH = 35
MAXIMUM_PROG_LENGTH = 50
PROGRESSION_LENGTH = 10


def generate_data():
    prog_start = randint(MINIMUM_PROG_START, MAXIMUM_PROG_START)
    prog_step = randint(MINIMUM_PROG_STEP, MAXIMUM_PROG_STEP)
    prog_length = randint(MINIMUM_PROG_LENGTH, MAXIMUM_PROG_LENGTH)
    progression = list(range(prog_start, prog_length, prog_step))
    progression = progression[:PROGRESSION_LENGTH]
    random_index = randint(0, len(progression) - 1)
    correct_answer = progression[random_index]
    progression[random_index] = '..'
    progression = list(map(str, progression))
    progression = ' '.join(progression)
    correct_answer = str(correct_answer)
    return progression, correct_answer
