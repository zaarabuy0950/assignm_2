"""5. Write a Python program to add 'ing' at the end of a given string (length should
be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the
string length of the given string is less than 3, leave it unchanged."""

a = input("enter a string:")
def asd(a):
    if len(a)<3 :
        return a
    elif(a[-3:]!='ing'):
        r= a +'ing'
        return r
    else:
        p = a + 'ly'
        return p
print(asd(a))



