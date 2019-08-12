# -*- coding: utf-8 -*-

class Parent(object):
    def call(self):
        print('Parent')


class Child(Parent):
    def call(self):
        print('Child')


class Example(object):
    pass
    # def call(self):
    #     print('Ex')


def call_obj(obj):
    obj.call()
#
#
# def sum_two_objects(one, two):
#     return one + two

child = Child()
call_obj(child)

parent = Parent()
call_obj(parent)

ex = Example()
call_obj(ex)


class ConstantFile:
    def open(self):
        pass

    def read(self):
        return "768"

    def close(self):
        pass

class NetworkFile(object):
    def __init__(self, url):
        pass

    def open(self):
        pass

    def read(self):
        return "768"

    def close(self):
        pass


class FilesystemFile(object):
    def __init__(self, filesystem_path):
        pass

    def open(self):
        pass

    def read(self):
        return "768"

    def close(self):
        pass


def process_text(testing):


    file.open()
    text = file.read()
    file.close()
    ...

    ...


def process_text1(testing):


    file.open()
    text = file.read()
    file.close()
    ...





def programma(testing):

    if testing == True:
        file = ConstantFile()
    elif <>:
        file = FilesystemFile('/some/path/to/file')
    else:
        file = NetworkFile("www.wikipedia.org")

    process_text(file)








