file = open('file.txt', 'w')
try:
    file.write(" Hello Mota!! ")
finally:
    file.close()

with open("file.txt", "a+") as file1:
    file1.write(' I Love you. ')

