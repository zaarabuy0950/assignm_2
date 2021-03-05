"""4. Write a Python program to get a single string from two given strings, separated
by a space and swap the first two characters of each string."""


a='abc'
b='xyz'

p=b[:2]+a[-1]
q=a[:2]+b[-1]
print(p + ' ' + q)












# a = 'abc'
# b = 'xyz'
# def fun(a,b):
#     p = b[:-1] + a[-1:]
#     q = a[0:2] + b[-1:]
#
#
#     return p+ ' ' +q
#
# print(fun('abc','xyz'))
#
