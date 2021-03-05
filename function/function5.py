"""5. Write a Python function to calculate the factorial of a number (a non-negative
integer). The function accepts the number as an argument."""


fact = 1
a1 = int(input("Enter a number: "))
for i in range(1 , a1+1):
    fact=fact*i
print(fact)
