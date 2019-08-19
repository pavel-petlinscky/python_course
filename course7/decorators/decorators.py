# -*- coding: utf-8 -*-
import time


def action_decorator(func):
    func_call_count = []
    def inner(*args, **kwargs):
        if len(func_call_count) == 0:
            print('Someone is going to', func.__name__)
            result = func(*args, **kwargs)
            func_call_count.append(1)
        else:
            result = func(*args, **kwargs)
        return result
    return inner

@action_decorator(enabled = True)  # try to uncomment me
def shout(text):
    print(text.upper(), '!!!!')

shout = action_decorator(enabled = True)(shout)


@action_decorator
def whisper(text):
    print(text.lower(), '...')

whisper('ABC')


@action_decorator
def say(something):
    something += '; was said.'
    print(something)


if __name__ == '__main__':
    # Basic functions:
    say('hi')
    whisper('Hello')
    shout('i am here')




@<MY_DECOR_NAME>
def sum1(a, b):
    return a+b

v = sum1(1, 2)

@<MY_DECOR_NAME>
def sum2(*args):
    return sum(args)

v1 = sum2(*list(range(0,1000)))

@<MY_DECOR_NAME>
def dv2(**kwargs):
    return kwargs.values()

v2 = dv2(**{'a': 1, 'b': 2})
