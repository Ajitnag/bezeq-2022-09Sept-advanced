#!/usr/bin/env python3

import signal


def handler(signum, frame):
    print(f'Got your signal!')


name = input('Enter your name: ').strip()

print(f'Hello, {name}!')
