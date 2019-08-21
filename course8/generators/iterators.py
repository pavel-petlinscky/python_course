# -*- coding: utf-8 -*-

x = iter([1, 2, 3])

print(next(x))
print(next(x))
print(next(x))
print(next(x))


class MyIterator:
    def __init__(self, some_list):
        self.__current = 0
        self.lst = some_list

    def __next__(self):
        if self.__current == len(self.lst):
            raise StopIteration()
        result = self.lst[self.__current]
        self.__current += 1
        return result

    def __iter__(self):
        return self


m = MyIterator([1, 2, 3, 4])

for el in m:
    print(el)