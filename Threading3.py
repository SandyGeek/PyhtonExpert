import threading
import time

ls = []


def func1(n):
    for i in range(1, n+1):
        print('From thread1:', i)
        time.sleep(0.6)


def func2(n):
    for i in range(1, n+1):
        print('From thread2:', i)
        time.sleep(0.6)


x = threading.Thread(target=func1, args=(5,))
x.start()
x.join()
y = threading.Thread(target=func2, args=(5,))
y.start()
y.join()