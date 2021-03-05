
"""6. Write a Python program to find the first appearance of the substring 'not' and
'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor'
substring with 'good'. Return the resulting string."""

def not_poor(asd):
    xnot=asd.find('not')
    xpoor=asd.find('poor')

    if xpoor >xnot and xnot > 0 and xpoor >0:
        asd=asd.replace(asd[xnot:(xpoor+4)], 'good')
        return asd
    else:
        return asd

print(not_poor('the lyrics is not that poor!'))
print(not_poor('the lyrics is poor!'))







