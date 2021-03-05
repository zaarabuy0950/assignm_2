"""41. Write a Python program to convert a tuple to a string"""

a1 = []
string = ''
n = int(input("Enter the no of ele: "))
for i in range(n):
    a1.append(input("Enter element: "))
a1 = tuple(a1)
string = str(a1)
print(string)