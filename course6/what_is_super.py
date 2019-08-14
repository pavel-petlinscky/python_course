# -*- coding: utf-8 -*-


class A:

    def __init__(self, k_val):
        self.k = k_val

    def return_k(self):
        return self.k

    def change_k(self, new_key):
        self.k = new_key


class Calc(object):
    def __init__(self, value):
        print('Calc constructor is called')
        self.value = value

    def count(self):
        res = self.value * 8 + 9
        return res

# c = Calc(1.4)
# c.count()

class ExtendedCalc(Calc):
    def __init__(self, value, x=1):
        super().__init__(value)
        # print('Calc constructor is called')
        # self.value = value
        print('Extender', self.value)
        x = 27 * x
        self.weight = x

    def count(self):
        a = self.weight + 1
        previous = super().count()
        #  previous = self.value * 8 + 9
        return -1 * self.weight * previous

    def count1(self):
        return 1

class ExtendedCalcPlus(ExtendedCalc):
    def count(self):
        super().count()

    def count1(self):
        super().count1()









e = ExtendedCalc(8, x=1.2)
e = ExtendedCalc(8, 4)
print(e.count())


class Car():
    def set_engine(self, eng):
        self.engine = eng

    def set_doors(self, doo):
        self.doors = doo

    def set_wheels(self, whl):
        self.wheels = whl

    def describe(self):
        print('{}, {}, {}'.format(self.engine,
                                  self.doors,
                                  self.wheels))


def set_wheels_to_car(car_to_modify):
    car_to_modify.set_wheels(4)


new_car1 = Car()
new_car1.set_doors(10)
new_car1.set_engine(5)
set_wheels_to_car(new_car1)
new_car1.describe()

new_car2 = Car()
new_car2.set_doors(10)
new_car2.set_engine(5)
set_wheels_to_car(new_car2)
new_car2.describe()


class A:
    #pass
    def __init__(self):
        self.x = 5

    def cnt(self):
        print('A')

class B:
    def __init__(self):
        self.x = 6

    def cnt(self):
        print('B')

class C(B, A):
    #pass
    def cnt(self):
        #A.cnt(self)
        #super(B, self).cnt()
        print('C')



class D(B, C):
    pass

c = C()
c.cnt()
