"""2.Write a Python function to sum all the numbers in a list.
Sample List : (8, 2, 3, 0, 7)
"""
from functools import  reduce
# a1 = input("enter a list:")
# a11 = a1.split()
# for i in range(0,len(a11)):
#     a11[i] = int(a11[i])
#
# print(a11)
#
# sum= lambda x,y:x+y
# result=reduce(sum,a11)
# print(f"the sum is:{result}")


asd = reduce(lambda x,y:x+y,[8,2,3,0,7])
print(f"sum is: {asd}")