"""12. Write a Python program to create a function that takes one argument, and
that argument will be multiplied with an unknown given number."""

a1 = int(input("Enter one argument: "))
n = int(input("Enter a unknown number: "))
def asd(n):
     return lambda a:a*n

qwe= asd(n)
print(qwe(a1))

