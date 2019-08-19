#!/usr/bin/env python
# -*- coding: utf-8 -*-


def switch(enabled=True):
    print('1')
    def decor(func):
        print('2')
        def wrapper(*args, **kwargs):
            print('3')
            if enabled is True:
                print('Function {} enabled'.format(func.__name__))
                return func(*args, **kwargs)
            else:
                print('Function {} disabled'.format(func.__name__))
                return None
        return wrapper
    return decor


@switch(enabled=True)
def some_logic(x, y):
    return x + y


print(some_logic(2, 3))
print(some_logic(2, 3))


@switch(enabled=False)
def some_logic(x, y):
    return x + y


print(some_logic(2, 3))



from functools import wraps

def my_decorator(f):
    def wrapper(*args, **kwds):
        print('Calling decorated function')
        return f(*args, **kwds)
    return wrapper


def better_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        print('Calling decorated function')
        return f(*args, **kwds)
    return wrapper


@my_decorator
def example():
    """Docstring"""
    print('Called example function')


@better_decorator
def example_2():
    """Docstring"""
    print('Called example function')


example()

print('example name', example.__name__)
print('example doc', example.__doc__)

print('example_2 name', example_2.__name__)
print('example_2 doc', example_2.__doc__)


def switcher(enabled=True):
    def param_better_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwds):
            print('Calling decorated function')
            return f(*args, **kwds)
        return wrapper
    return param_better_decorator


@switcher()
def example_3():
    """Docstring"""
    print('Called example function')

print('example_3 name', example_2.__name__)
print('example_3 doc', example_2.__doc__)
