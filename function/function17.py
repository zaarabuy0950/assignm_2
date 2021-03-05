"""17. Write a Python program to find if a given string starts with a given character
using Lambda."""

a1 = input("Enter a character: ")
a2 = input("Enter a string: ")

starts_with_char = list(filter(lambda x:x.startswith(a1),a2))
not_start = list(filter(lambda x:not x.startswith(a1),a2))
if starts_with_char:
   print(f"The string with given char {a1} is: {a2}")
else:
   print(f"The string with given char {a1} is not in string: {a2}")

