
"""6. Write a Python function to check whether a number is in a given range."""

a = int(input("Enter the start_range: "))
b = int(input("Enter the end_range: "))
n = int(input("Enter the number: "))
if n in range(a,b):
    print(f"{n} is in range {a,b}")
else:
    print(f"{n} is out of range {a,b}")
