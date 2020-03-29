import threading
import time


def func(y, z, a):
    print('START.....')
    time.sleep(0.45)
    print('DONE....')
    print(y, z, a)


x = threading.Thread(target=func, args=(4, 5, 2))
x.start()
print(threading.active_count())
time.sleep(1)
print('Finally complete....')

