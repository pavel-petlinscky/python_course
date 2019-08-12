# -*- coding: utf-8 -*-


class Example(object):
    def __init__(self):
        self.a = 1
        self._b = 2
        self.__c = 3
        print('{} {} {}'.format(
            self.a, self._b, self.__c))

    def call(self):
        print('Called!')

    def _protected_method(self):
        print('Protected method')

    def __private_method(self):
        print('Private method')


class Inh(Example):
    def nnn(self):
        self._b = 5
        self.__c = 6
        self._protected_method()
        self.__private_method()
        #print(self._b, self.__c)



example = Example()
print(example.a)
print(example._b)


try:
    print(example.__c)
except AttributeError as ex:
    print(ex)
