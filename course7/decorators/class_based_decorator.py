#!/usr/bin/env python
# -*- coding: utf-8 -*-

import functools


class MyDecorator:
    def __init__(self, argument):
        self.arg = argument

    def __call__(self, fn):
        # @functools.wraps(fn)
        def decorated(*args, **kwargs):
            print('In my decorator before call, with arg {}'.format(self.arg))
            fn(*args, **kwargs)
            print('In my decorator after call, with arg {}'.format(self.arg))
        return decorated



@MyDecorator('some other func!')
def some_other_function():
    print('in some other function!')








@MyDecorator()
def foo():
    print('foo')

foo()

@MyDecorator
def sum(x, y):
    return x + y
# sum(1, 2)




class Foo():
    @MyDecorator("in Foo class!")
    def bar(self, x, y):
        print('in bar! {}'.format(x+y))





@MyDecorator('some other func!')
def some_other_function():
    print('in some other function!')

Foo().bar()
some_other_function()

