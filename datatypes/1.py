"""1. Write a Python program to count the number of characters (character
frequency) in a string. Sample String : google.com'"""

import operator
str = input("Ënter a string: ")
d = {}
for x  in str:
   if x in d.keys():
       d[x]+=1

   else:
       d[x] = 1


print(dict(sorted(d.items(),key=operator.itemgetter(1),reverse=True)))





