
"""19. Write a Python program to get the smallest number from a list."""

a=input("ente a number:")
asd=a.split()
for i  in range(len(asd)):
    asd[i]=int(asd[i])
print(min(asd))