# -*- coding: utf-8 -*-


# pythontutor
def fib():
    """
    :return: 0, 1, 1, 2, 3, 5, 8, 13, 21 ...
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def gen():
    yield 'value'


x = gen()
next(x)
next(x)  # OOPS
next(x)


def gen():
    yield 'value'
    yield 'value'
    yield 'value'


x = gen()
next(x)
next(x)  # OOPS
next(x)


def gen():
    yield 'value'
    return 'some'  # Not return, just message of stop iter


def gen():
    while True:
        yield 'value'


def foo(*args, **kwargs):
    """

    :param args: send to function bar, see it signature
    :param kwargs:
    :return:
    """


def gen():
    v = ''
    for c in v:
        yield c


def cities():
    arr = [
        'Moscow',
        'Novosibirsk',
        'Perm',
        'Irkutsk',
        'Tula',
    ]
    return iter(arr)


if __name__ == '__main__':
    cities_gen = cities()

    while True:
        try:
            print(next(cities_gen))
        except StopIteration:
            break

    try:
        print(next(cities_gen))  # create new cities()
    except StopIteration:
        print('Will not work')

    new_cities = cities()
    print(next(new_cities))
    print(list(new_cities))

    fib_gen = fib()
    for index, _ in enumerate(range(10)):
        print(index, next(fib_gen))
