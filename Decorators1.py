def fun1(f):
    def fun2():
        f()
        print('Printed from fun2()')
    # f()
    return fun2


def fun3():
    print('Printed from fun3()')


# x = fun1(fun3)
# x()
fun1(fun3)
print(fun1(fun3))
print(fun1(fun3()))
print(fun3)
