"""43. Write a Python program to remove an item from a tuple."""


a1 = input("Enter list of tuple: ")
a2 = tuple(x for x in a1.split())
asd = list(a2)
asd.remove(input("Enter an element to remove: "))
a = tuple(asd)
print(a2)




# tuplex = (1, 2, 3, 4, 5, 8, 9)
# tuplex = list(tuplex)
# for x in tuplex:
#   if (x % 2 == 1):
#      tuplex.pop(tuplex.index(x))
# tuplex = tuple(tuplex)
# print(tuplex)