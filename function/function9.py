"""9. Write a Python function that takes a number as a parameter and check the
number is prime or not."""

a1 = int(input("Enter the number: "))
if a1 > 1:
    for i in range(2, a1):
        if a1 % i == 0:
            print(f"{a1} is not a prime number")
            break
        else:
            print(f"{a1} is a prime number")
            break




