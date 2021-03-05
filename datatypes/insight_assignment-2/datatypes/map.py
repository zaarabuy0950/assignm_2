# def add_two(x):
#         return x+2
#
# r=map(add_two,[1,2,3,4])
# print(list(r))
#

# def is_even(x):
#         if x%2==0:
#                  return true
#         return false
# r=filter(is_even,[1,2,3,4])
#
# print(list(r))#



from functools import reduce
def mul(x,y):
        return x*y
print(reduce(mul,[1,2,3,4]))