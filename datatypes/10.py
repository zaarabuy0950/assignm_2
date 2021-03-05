
"""10. Write a Python program to remove the characters which have odd index
values of a given string."""

s1 = str(input("Enter a string :"))
def fun(s1):
    r = s1[0::2]
    return r
print(fun(s1))




#
# a= input('enter a string:')
# b=''
# for i in range(len(a)):
#         if (i % 2==0):
#             b=b+a[i]
#
# print(b)