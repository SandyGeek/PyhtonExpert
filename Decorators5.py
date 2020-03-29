def mainfunc(f):
    def wrapper():
        print('Printed from wrapper()')
        f()
    return wrapper


def decfun2():
    print('Printed from defunc2()')


@mainfunc
def decfun3():
    print('Printed from defunc3()')


decfun3()
decfun2()
