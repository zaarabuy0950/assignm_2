"""26. Write a Python program to insert a given string at the beginning of all items in
a list."""

# a=[1,2,3,4,]
# print(['emp{0}'.format(i) for i in a])


a1 = [1,2,3,4]
str1 = "emp"
for i in range(0,len(a1)):
               a1[i] = str(a1[i])
               a1[i] = str1 + a1[i]
print(a1)
