from random import randint


TEXT_GAME = 'Answer "yes" if given number is prime. Otherwise answer "no".'
RANDOM_MIN_VALUE = 1
RANDOM_MAX_VALUE = 100


def is_prime(n):
    if n <= 1:
        return False
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            return False
    return True


def generate_data():
    random_number = randint(RANDOM_MIN_VALUE, RANDOM_MAX_VALUE)
    if is_prime(random_number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return random_number, correct_answer
