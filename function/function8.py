"""Write a Python function that takes a list and returns a new list with unique
elements of the first list."""

a1 = input("Enter a list: ")
a2 = a1.split()
s1 = sorted(set(a2))
for i in range(0,len(s1)):
    s1[i] = int(s1[i])
print(s1)