#!/usr/bin/env python3

import signal


def handler(signum, frame):
    print(f'Too late!')


signal.signal(signal.SIGINT, handler)


name = input('Enter your name VERY VERY FAST: ').strip()

print(f'Hello, {name}!')
