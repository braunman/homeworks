# -*- coding: utf-8 -*-

from contextlib import contextmanager
from time import time, sleep


class Lock(object):

    def __init__(self):
        self.lock = False
        print("Object 'Lock' create, lock = {0}".format(self.lock))

    def __enter__(self):
        self.lock = True
        print("Now lock = {0}".format(self.lock))

    def __exit__(self, *arg):
        self.lock = False
        print("Exit and return lock to {0}".format(self.lock))


@contextmanager
def no_exceptions():
    try:
        yield
    except Exception as e:
        print("Alarm: {0}".format(e))


@contextmanager
def time_it():
    time_begin = time()
    yield
    print("Execution time {}".format(time() - time_begin))


if __name__ == '__main__':

    l = Lock()
    with l:
        print(l)

    with no_exceptions():
        1 / 0

    with time_it():
        sleep(2)
