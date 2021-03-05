"""11. Write a Python program to count the occurrences of each word in a given
sentence."""

import operator
str = input("Enter the sentence: ")
d = {}
for x in str:
   if x in d.keys():
       d[x]+=1

   else:
       d[x] = 1


print(dict(sorted(d.items())))
