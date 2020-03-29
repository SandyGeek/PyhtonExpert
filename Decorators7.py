def mainfunc(f):
    def wrapper(*arguments, **kwargs):
        print('Printed from wrapper()')
        rv = f(*arguments, **kwargs)
        return rv
    return wrapper


@mainfunc
def decfun2(x, y, z):
    print('Printed from defunc2()')
    print(x, y, z, " is Printed from defunc2()")
    return z


@mainfunc
def decfun3():
    print('Printed from defunc3()')


z = decfun2(5, 6, 7)
print(z)
decfun3()
