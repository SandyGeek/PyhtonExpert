class MyMetaParentClass(type):
    def __new__(mcs, class_name, bases, attrs):
        print(attrs)
        a = {}
        for name, val in attrs.items():
            if name.startswith("__"):
                a[name] = val
            else:
                a[name.upper()] = val
        print(a)
        return type(class_name, bases, attrs)


class MyMetaSubClass(metaclass=MyMetaParentClass):
    x = 5
    y = 9
