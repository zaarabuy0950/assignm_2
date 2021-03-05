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



