"""32. Write a Python script to generate and print a dictionary that contains a
number (between 1 and n) in the form (x, x*x)."""

a=int(input('enter a number:'))
asd={}
for i in range(1,a+1):
    asd[i]=i*i
print(asd)