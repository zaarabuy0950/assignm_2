"""44. Write a Python program to slice a tuple"""

start = int(input("Enter the start: "))
stop = int(input("Enter the stop: "))
step = int(input("Enter the step size: "))
a1 = input("Enter list of tuple: ")
a2 = tuple(int(x) for x in a1.split())
a1_slice =a2[start:stop:step]
print(a1_slice)