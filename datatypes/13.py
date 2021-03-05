"""13. Write a Python program that accepts a comma separated sequence of words
as input and prints the unique words in sorted form (alphanumerically)."""

# a = input('enter a word:')
# asd = a.split(",")
#
# print(sorted(asd))

a=input('enter a word:')
def fun(a):
    asd = a.split(",")
    return sorted(asd)
print(fun(a))