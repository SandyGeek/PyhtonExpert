from contextlib import contextmanager


@contextmanager
def file(filename, method):
    print("From file() start")
    fileobj = open(filename, method)
    yield fileobj
    fileobj.close()
    print("From file() end")


with file('file.txt', 'a') as f:
    f.write(" Love you Munii ")
    print("From with")
