"""20. Write a Python program to find intersection of two given arrays using
Lambda."""

arr1 = input("Enter the first array: ")
a1 = arr1.split()
for i in range(0,len(a1)):
    a1[i] = int(a1[i])
print(a1)
arr2 = input("Enter second array: ")
a2 = arr2.split()
for i in range(0,len(a2)):
    a2[i] = int(a2[i])
print(a2)
result = list(set(filter(lambda x: x in arr1,arr2)))
print(f"Inserted array: {result}")


