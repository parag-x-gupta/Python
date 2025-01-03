#write a program to switch values of two variables

a = int(input("Input the first variable : "))
b = int(input("Input the second variable : "))

c = a
a = b
b = c

print(f"First variable is : {a}\n Second Variable is {b}")