
"""Write a Python program to sum all the items in a list."""

from functools import reduce
a= input('Enter a list:')
a1 = a.split()
for i in range(len(a1)):
   a1[i] = int(a1[i])

asd=lambda x,y:x+y
res=reduce(asd,a1)

print(res)