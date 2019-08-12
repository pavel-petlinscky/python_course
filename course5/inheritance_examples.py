# -*- coding: utf-8 -*-


# All classes have the smae base class: object

class Test:
    pass


class Test(object):  # it is the same as the code above (py3 only)
    pass


# Classes can inherit other classes

#class Person(object):
class Person:
    biological_name = 'homo sapiens'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        print('Walking...')

    def say_hello(self):
        print('I am a person', self.name, self.age)


class Student(Person):

    def say_hello(self):
        print('I am a student', self.name, self.age)








s = Student('Petr', 23)
print(s.biological_name)
s.walk()
s.say_hello()



class Child(Person):

    def __init__(self, name, age):
        if age > 18:
            raise ValueError('ЭТО БЫЛ НЕ НЕСКАФЕ!')

        self.name = name
        self.age = age

    def walk(self):
        raise ValueError('Can not walk')

    def say_hello(self):
        raise ValueError('Can not talk')

    def crawl(self):
        print('Haha!')


child = Child('Steve Jr', 1)
print(child.biological_name)


class Calc:
    def __init__(self, number):
        self.number = number

    def calc_and_print(self):
        value = self.calc_value()
        self.print_number(value)

    def calc_value(self):
        return self.number * 10 + 2

    def print_number(self, value_to_print):
        print('!!!!')
        print('Number is ', value_to_print)
        print('!!!!')


class CalcExtraValue(Calc):
    def calc_value(self):
        return self.number - 100


c = Calc(4)
c.calc_and_print()

c1 = CalcExtraValue(4)
c.calc_and_print()





class Person(object):
    biological_name = 'homo sapiens'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        if self.age > 3:
            print('Walking...')
        else:
            raise ValueError('Can not walk')

    def say_hello(self):
        if self.age < 3:
            raise ValueError('Can not talk')
        elif self.age > 23:
            print('I am a person', self.name, self.age)
        else:
            print('I am a student', self.name, self.age)

    def crawl(self):
        if self.age < 3:
            print('Haha!')
        else:
            raise ValueError('Can not crawl')





class A:
    x = 5
    def f(self):
        pass


class B:
    def f(self):
        pass

class C:
    def f(self):
        pass

class D(A, B, C):
    pass




#def gen_person(age, name):




