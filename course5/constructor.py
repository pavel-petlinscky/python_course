# -*- coding: utf-8 -*-


# Constructor is called when new instance is created
class TestClass:
    data = 5

    def __init__(self):
        print("Init called")
        self.data = 1


t = TestClass()

t1 = TestClass()




class Car:
    speed = 0

    def __init__(self, color,
                 transmission='Auto',
                 x=10):
        if x == 0:
            raise RuntimeError
        car = Car('yellow', x-1)



        # print('Constructor is called!')
        # print('Self is the object itself!', self)
        # self.color = color
        # self.transmission = transmission
        #
        # car = Car('yellow')

        # HERE ENGINE AND TRANSMISSION COMPAT CHECK







# Constructor can have parameters

class Table:
    def __init__(self, number_of_legs):
        print('New table has {} legs'.format(
            number_of_legs))


t = Table(4)
t1 = Table(3)




# But we need to save them into the fields!

class Chair:
    def __init__(self, color):
        self.color = color


c = Chair('green')
print(c, c.color)

c1 = Chair('Red')
print(c1.color)
print('variable c did not change!', c.color)
