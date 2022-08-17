#!/usr/bin/env python
from brain_games.games.engine import start_games
from brain_games.games import prime


def main():
    start_games.start(prime)


if __name__ == '__main__':
    main()
