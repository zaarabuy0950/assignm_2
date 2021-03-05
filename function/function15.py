
"""15. Write a Python program to filter a list of integers using Lambda."""

from functools import reduce
a1 = input("Enter a list: ")
a2 = a1.split()
for i in range(0,len(a2)):
    a2[i] = int(a2[i])
print(a2)
int_sort = lambda x:x/2>0
result = filter(int_sort,a2)
print(list(result))
