
"""12. Write a Python script that takes input from the user and displays that input
back in upper and lower cases."""


a1 = str(input("Enter a string :"))
def fun(a1):
    r1 = a1.upper()

    r2 = a1.lower()
    return r1 , r2
print(fun(a1))
