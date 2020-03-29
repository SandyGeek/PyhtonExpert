x = [i ** 2 for i in range(100)]
for el in x:
    print(el)


class Gen:
    def __init__(self, n):
        self.n = n
        self.last = 0

    def __next__(self):
        return self.next()

    def next(self):
        if self.last == self.n:
            raise StopIteration
        rv = self.last ** 2
        self.last += 1
        return rv


g = Gen(100)
while True:
    try:
        print(next(g))
    except StopIteration:
        break

