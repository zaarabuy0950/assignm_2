"""33. Write a Python script to print a dictionary where the keys are numbers
between 1 and 15 (both included) and the values are square of keys"""

n = int(input("Enter the end of list: "))
dict1 = {}
for i in range(1,n):
  dict1[i]=i**2
print(dict1)

