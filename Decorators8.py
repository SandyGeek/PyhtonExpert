import time


def timer(f):
    def wrapper(*args, **kwargs):
        start = time.time()
        rv = f()
        total = time.time() - start
        print('Total time : ', total)
        return rv
    return wrapper


@timer
def test1():
    for _ in range(100000):
        pass


@timer
def test2():
    time.sleep(5)


test1()
test2()
