#!/usr/bin/env python
from brain_games import start_games
from brain_games.games import even


def main():
    start_games.start(even)


if __name__ == '__main__':
    main()
