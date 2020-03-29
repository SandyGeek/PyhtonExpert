import sys
x = [i ** 2 for i in range(100)]


def gen(n):
    for i in range(n):
        yield i**2


g = gen(100)

"""
for i in g:
    print(i)

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

"""
print(sys.getsizeof(x))
print(sys.getsizeof(g))
