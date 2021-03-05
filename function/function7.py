"""7. Write a Python function that accepts a string and calculate the number of
upper case letters and lower case letters."""

string1 = input("Enter a string: ")
low = 0
upp = 0
for i in string1:
    if(i.islower()):
        low = low + 1
    elif(i.isupper()):
        upp = upp + 1
print(upp)
print(low)


