#!/usr/bin/env python3

import signal


class TooSlowException(Exception):
    pass


def handler(signum, frame):
    print(f'Too late!')
    raise TooSlowException('ha ha!')


signal.signal(signal.SIGALRM, handler)

signal.alarm(3)   # in another 3 seconds, send this signal

try:
    name = input('Enter your name VERY VERY FAST: ').strip()
    print(f'Hello, {name}!')
except TooSlowException as e:
    print('Too slow!')
    
