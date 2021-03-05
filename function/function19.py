"""19. Write a Python program to create Fibonacci series upto n using Lambda."""

from functools import reduce

n = int(input('Enter the Number of terms'))
def fib(n):
    return reduce(lambda x, _: x+[x[-1]+x[-2]], range(n-2), [0, 1])
print(fib(n))











# def fib(count):
#     lst = [0, 1]
#     any(map(lambda _: lst.append(sum(lst[-2:])), range(2, count)))
#     return lst[:count]
# print(fib(int(input())))


