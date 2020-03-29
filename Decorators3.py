def mainfunc(f):
    print('Execution started from mainfunc()')

    def wrapper(x):
        print(x)
        f()
        print('Printed from wrapper()')
    print('Execution ended from mainfunc()')
    return wrapper


def decfun2():
    print('Printed from defunc2()')


def decfun3():
    print('Printed from defunc3()')


# a = mainfunc(decfun3)
# mainfunc(decfun3())
mainfunc(decfun3)
# print(a(5))
# a(5)
