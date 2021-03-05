"""13. Write a Python program to sort a list of tuples using Lambda."""

def a1(tup):
    tup.sort(key=lambda x:x[1])
    return tup

tup=[('ram',10),('hari',4),('shyam',14)]

print(a1(tup))