def mainfunc(f):
    def wrapper(x):
        print(x)
        print('Printed from wrapper()')
        f()
    return wrapper


# @mainfunc
def decfun2():
    print('Printed from defunc2()')


@mainfunc
def decfun3():
    print('Printed from defunc3()')


decfun3(5)
decfun2()
