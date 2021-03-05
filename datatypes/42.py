"""42. Write a Python program to convert a list to a tuple."""

list1 = input("Enter a list :")
a1 = list1.split()
for i in range(0,len(a1)):
    a1[i] = int(a1[i])
asd = tuple(a1)
print(asd)