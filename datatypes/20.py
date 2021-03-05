"""20. Write a Python program to count the number of strings where the string
length is 2 or more and the first and last character are same from a given list of
strings.
Sample List : ['abc', 'xyz', 'aba', '1221']"""

list1 = ['abc', 'xyz','aba','1221']

def fun(list1):
    count = 0
    for i in list1:
         if len(i) > 1 and i[0] == i[-1]:
             count += 1
             return count


print(fun(list1))