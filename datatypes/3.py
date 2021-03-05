"""3. Write a Python program to get a string from a given string where all
occurrences of its first char have been changed to '$', except the first char itself.
Sample String : 'restart'"""


def fun(s1):
 a = s1[0]
 s1 = s1.replace(a, '$')
 s1 = a + s1[1:]
 return s1

print(fun('restart'))