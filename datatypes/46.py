"""46. Write a Python program to find the length of a tuple"""


t = input("Enter list of tuple: ")
a = tuple(x for x in t.split())
len_tup = len(a)
print(a)
print(f"Length of given tuple is: {len_tup}")













# a1=tuple('helloworld')
# print(a1)
# print(len(a1))