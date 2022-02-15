#!/usr/bin/env python
import sys

from src.app import run_server


def main(args: str = []) -> None:
    if args[0] == 'run':
        run_server()

if __name__ == '__main__':
    main(args=sys.argv[1:])
