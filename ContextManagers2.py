class FileOperate:
    def __init__(self, filename, method):
        self.file = open(filename, method)

    def __enter__(self):
        print("From __enter__()")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'{exc_type}, {exc_val}, {exc_tb}')
        print("From __exit__()")
        self.file.close()
        try:
            if type == Exception:
                print("Exception occurred.")
        finally:
            print("Not done")


with FileOperate("file.txt", "a") as file1:
    file1.write(' I Love you. ')
    print("From with function")
    raise Exception()
