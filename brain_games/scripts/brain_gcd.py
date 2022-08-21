#!/usr/bin/env python
from brain_games import start_games
from brain_games.games import gcd


def main():
    start_games.start(gcd)


if __name__ == '__main__':
    main()
