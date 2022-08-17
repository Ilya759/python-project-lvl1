#!/usr/bin/env python
from brain_games.games.engine import start_games
from brain_games.games import calc


def main():
    start_games.start(calc)


if __name__ == '__main__':
    main()
