"""21. Write a Python program to get a list, sorted in increasing order by the last
element in each tuple from a given list of non-empty tuples.
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]"""

a1 = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
def asd(data):
    return data[1]
print(sorted(a1,key=asd))