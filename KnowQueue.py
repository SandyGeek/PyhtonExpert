from queue import Queue as myqueue
import inspect


# q = myqueue()
# print(q)
# print(inspect.getsource(myqueue))


class MyQueueClass(myqueue):
    # def __str__(self):
    #    return f'Printed by __str__() method of {self.__class__}.'

    def __repr__(self):
        print(self.qsize())
        return f'Printed by __repr__() with Queue size of {self._qsize()}'

    def __add__(self, item):
        self.put(item)
        self._put(item)

    def __sub__(self, item):
        self.get(item)


q = MyQueueClass()
q + 5
q + 6
a = q - 6
print(a)
print(q)
print(MyQueueClass)
print(type(MyQueueClass))
