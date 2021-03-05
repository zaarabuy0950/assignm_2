"""40. Write a Python program to add an item in a tuple."""

a1 = input("Enter list of tuple: ")
a2 = tuple((x) for x in a1.split())
l = list(a2)
l.append(input("Enter an element to add: "))
a2 = tuple(l)
print(a2)















# a1=(1,6,4,3)
# print(a1)
# a1=a1[:5]
# print(a1)
