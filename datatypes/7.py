
"""7. Write a Python function that takes a list of words and returns the length of the
longest one"""


list1 = input("Enter a list :")
a2 = list1.split()
for i in range(0,len(a2)):
    a2[i] = int(a2[i])
print(f"Maximum number: {max(a2)}")








#
#
# def longest_word(longest):
#     word_len=[]
#     for n in longest:
#         word_len.append((len(n), n))
#     word_len.sort()
#     return word_len[-1][0], word_len[-1][1]
# result =longest_word(["hello","fund","dashboard","management"])
# print("\nlongest word:",result[1])
# print("\nlength of the longest wprd:",result[0])
