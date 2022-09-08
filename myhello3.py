#!/usr/bin/env python3

import signal


class TooSlowException(Exception):
    pass


def handler(signum, frame):
    print(f'Too late!')
    raise TooSlowException('ha ha!')


signal.signal(signal.SIGINT, handler)


name = input('Enter your name VERY VERY FAST: ').strip()

print(f'Hello, {name}!')