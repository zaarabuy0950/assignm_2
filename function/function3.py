"""Write a Python function to multiply all the numbers in a list.
Sample List : (8, 2, 3, -1, 7)"""

from functools import  reduce
# a1 = input("enter a list:")
# a11 = a1.split()
# for i in range(0,len(a11)):
#     a11[i] = int(a11[i])
#
# print(a11)
#
# mul= lambda x,y:x*y
# result=reduce(mul,a11)
# print(f"The Multipicationis:{result}")

asd = reduce(lambda x,y:x*y,[8,2,3,-1,7])
print(f"Multipication is: {asd}")