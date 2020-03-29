# Whenever the (line number 33) decfun3 is called, it actually maps with wrapper function.
# So, it is important to pass the same kind of variable which is passed through wrapper and decfun3 function


def decfun1(f):
    def wrapper(x):
        print(x)
        f()
        print('Printed from decfun2()')
    return wrapper


@decfun1
def decfun3():
    print('Printed from fun3()')


decfun3(5)