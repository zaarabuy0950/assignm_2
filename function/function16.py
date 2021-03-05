"""16. Write a Python program to square and cube every number in a given list of
integers using Lambda."""

a1 = input("Enter a list: ")
a2= a1.split()
for i in range(len(a2)):
    a2[i] = int(a2[i])
print(f"Given list : {a2}")

square = lambda x:x**2
cube = lambda x:x**3

r1 = list(map(square,a2))
r2 = list(map(cube,a2))

print(f"Square of given list: {r1}")
print(f"Cube of given list: {r2}")
