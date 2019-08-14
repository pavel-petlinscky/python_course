#!/usr/bin/env python
# -*- coding: utf-8 -*-


class MyClass(object):
    def __new__(cls, x, y, z):
        print("constructing instance with arguments:")
        print("    ", cls, x, y, z)
        instance = super(MyClass, cls).__new__(cls)
        return instance

    def __init__(self, a, b, c):
        print("initializing instance with arguments:")
        print("    ", self, a, b, c)

        self.a = a
        self.b = b
        self.c = c


inst = MyClass(23, 42, 'spam')
