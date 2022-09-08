#!/usr/bin/env python3

import signal


def handler(signum, frame):
    print(f'Got your signal!')


signal.signal(signal.SIGUSR1, handler)


name = input('Enter your name: ').strip()

print(f'Hello, {name}!')
