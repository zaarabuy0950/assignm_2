"""15. Write a Python function to insert a string in the middle of a string.
Sample function and result :"""

def mstring(str1, str2):
    length = int(len(str1)/2)
    print(str1[:length] + str2 + str1[length:])
print(mstring(input("string1: "),input("string2: ")))



