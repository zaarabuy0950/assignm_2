"""38. Write a Python program to remove a key from a dictionary."""

dict1 = {}
n = int(input("Enter the number of dictionary: "))
for i in range(n):
    k = int(input("Enter the key: "))
    v = int(input("Enter the value: "))
    dict1.update({k:v})
print(dict1)
print((dict1.keys()))