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
