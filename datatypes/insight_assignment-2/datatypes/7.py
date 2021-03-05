def longest_word(longest):
    word_len=[]
    for n in longest:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][0], word_len[-1][1]
result =longest_word(["hello","fund","dashboard","management"])
print("\nlongest word:",result[1])
print("\nlength of the longest wprd:",result[0])