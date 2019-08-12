# -*- coding: utf-8 -*-


# This is a simplest class

class Car:
    pass


c = Car()
print(c, type(c))


# Classes can have variables called fields
class Room:
    number = 'Room 34'
    floor = 4


r = Room()
r1 = Room()
print(r.number, r1.number)
print(r.floor, r1.floor)

# You can modify values:
r.number = 12
r.floor = '5 floor'
print(r.number, r1.number)
print(r.floor, r1.floor)






# Classes can have functions inside: it's called a method

class Car:
    speed = 0

    def accelerate(self):
        self.speed = self.speed + 3

    def accelerate_to(self, speed_delta):
        self.speed = self.speed + speed_delta

    def stop(self):
        self.speed = self.speed - 3

    # def mass(self):
    #     return 35

def foo():
    pass


class Door:
    def open(self):  # note that `self` is the object itself!
        print('self is', self)
        print('Door is opened!')
        self.opened = True   # not so cool style


d = Door()
d.open()
print(d.opened)

d1 = Door()
d1.open()






# Methods can accept params (as functions)

class Terminal:
    def hello(self, user_name):
        print('self is the object itself', self)
        print('Hello,', user_name)


t = Terminal()
t.hello('Nikita')
t.hello('Vova')


# Classes can have both methods and fields
class Window:
    is_opened = False

    def open(self):
        self.is_opened = True
        print('Window is now ', self.is_opened)

    def close(self):
        self.is_opened = False
        print('Window is now ', self.is_opened)


w = Window()
w1 = Window()

print('Initial state', w.is_opened, w1.is_opened)

w.open()
print('New state', w.is_opened, w1.is_opened)

w.close()
print('New state', w.is_opened, w1.is_opened)
