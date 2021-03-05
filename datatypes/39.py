
"""39. Write a Python program to unpack a tuple in several variables."""


a1 = input()
a2 = tuple(int(x) for x in a1.split())
print(f"Tuple unpacking: {a1}")
print(f"Tuple packing: {a2}")























# a1=(1,6,4,3)
# a,b,c,d=a1
# print(a)
# print(b)
# print(c)
