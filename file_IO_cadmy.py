# with open("textExpt.txt") as file:
#     x = file.read()  # reads the file in one go and stores it as a string
#     print("Read Function")
#     print(type(x))
#     print(x)

# with open("textExpt.txt") as file2:
#     y = file2.readline()
#     print("Readline Function")
#     print(y)

with open("textExpt.txt") as file3:
    print('Pointer at the beginning:', file3)
    print("File 3 :", list(file3))
    print('Pointer at the ending:', list(file3))
    # z = file3.readlines()
    # print("Z:", file3)
    # for line in file3:
    #     print(line)
    #     print(type(line))

with open("textExpt.txt") as file3:
    print('Pointer at the beginning:', file3)
    for line in file3:
        print(line, end='')
    file3.seek(0)
    print('Pointer at the ending:', list(file3))