"""25. Write a Python program to check whether all dictionaries in a list are empty or
not."""


a=[{},{},{}]
b=[{1,2},{},{}]
print(all(not d for d in a))

print(all(not d for d in b))