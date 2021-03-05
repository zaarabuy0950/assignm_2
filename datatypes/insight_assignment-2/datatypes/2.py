a=input("enter a string:")

def asd(a):
    if len(a)<2:
        return "empty string"
    else:
        return  a[0:2] + a[-2:]



print(asd(a))