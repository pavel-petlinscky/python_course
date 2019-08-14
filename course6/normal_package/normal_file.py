# -*- coding: utf-8 -*-
import random

class MyClass:
    pass


def my_function():
    random.randint(5)
    print('My function is working!')


def special_function():
    print('Another special function')

def run_only_if_im_entry_point():
    print('JJJ')

GLOBAL_VAR = 12



print('__name__ is ', __name__)

if __name__ == '__main__':
    run_only_if_im_entry_point()
    my_function()







