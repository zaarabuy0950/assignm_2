"""11. Write a Python program to create a lambda function that adds 15 to a given
number passed in as an argument, also create a lambda function that multiplies
argument x with argument y and print the result."""

a1 = int(input("Enter any number: "))
a2 =  int(input("Enter any number: "))
add = lambda a1:a1+15
mul = lambda a1,a2:a1*a2
print(add(a1))
print(mul(a1,a2))
