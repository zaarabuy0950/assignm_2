
"""18. Write a Python program to get the largest number from a list."""


a=input("ente a number:")
asd=a.split()
for i  in range(len(asd)):
    asd[i]=int(asd[i])
print(max(asd))