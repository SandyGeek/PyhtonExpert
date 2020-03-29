# from inspect import _check_instance
import inspect
import datetime
today = datetime.datetime.now()

# Prints readable format for date-time object
print(str(today))

# prints the official format of date-time object
print(repr(today))

x = [1, 5, 6, 8]
print(type(x))
print(id(x))


def Maa():
    class Sandy:
        def __init__(self, name):
            self.name = name
            # print(name)
            print('Printed from Sandy _init_()')

        def __repr__(self):
            return f'{self.name} {self.__class__} did it.'

        def __add__(self, other):
            self.name = self.name + other
            print(self.name)

    class Muni:
        def __init__(self):
            print('Printed from Muni _init_()')

    s = Sandy('MyName')
    m = Muni()
    print(s)
    print(m)
    print(Sandy)
    return Sandy


y = Maa()
z = y('Sandip')
print(z + 'ME')
# print(z)
# print(y)
# print(type(y))
# print(y('Ankita'))
# print(y('Sandy').name)

"""
print(inspect.getsource(queue))
print(inspect.getmembers(queue))

"""
