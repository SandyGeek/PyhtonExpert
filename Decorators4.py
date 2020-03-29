def mainfunc(f):
    def wrapper():
        print('Printed from wrapper()')
        f()
    return wrapper


def decfun3():
    print('Printed from defunc3()')


decfun3 = mainfunc(decfun3)
decfun3()
mainfunc(decfun3)
