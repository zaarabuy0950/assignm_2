
"""22. Write a Python program to remove duplicates from a list."""


a=input('enter a list:')
asd=a.split()
# c = set(asd)
# d =list(c)
# print(d)

print(sorted(list(set(asd))))
