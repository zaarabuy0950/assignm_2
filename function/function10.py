"""10. Write a Python program to print the even numbers from a given list.
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]"""



a1= input("Enter a list: ")
a2= a1.split()
for i in range(len(a2)):
   a2[i] = int(a2[i])
print(a2)

even = lambda x:x % 2 == 0
result = list(filter(even,a2))
print(f"Ëven number list are : {result} ")