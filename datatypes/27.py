
"""27. Write a Python program to replace the last element in a list with another list.
Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]"""



a1 = [1,3,5,7,9,10]
a2 = [2,4,6,8]
a3 = a1[0:5]
a4= a1+ a2

print(a4)


# a1=[1,3,5,7,9,10]
# a2=[2,4,6,8]
#
# a1[-1:]=a2
#
# print(a1)