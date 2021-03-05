
"""45. Write a Python program to find the index of an item of a tuple."""

t = input("Enter tuple elements: ")
a = tuple((x) for x in t.split())
search_elem = input("Search index of: ")
res = a.index(search_elem)
print(f"Index[{search_elem}] is {res}")















# a1=('a', 'e', 'i', 'o', 'g', 'l', 'i', 'u')
# a2=a1.index('o')
# print(a2)

