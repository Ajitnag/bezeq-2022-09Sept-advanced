#!/usr/bin/env python3

import signal


def handler(signum, frame):
    print(f'Got your control-C!')


signal.signal(signal.SIGINT, handler)


name = input('Enter your name VERY VERY FAST: ').strip()

print(f'Hello, {name}!')
