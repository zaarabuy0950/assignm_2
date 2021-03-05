# # def decorate_me(func):
# #     def inner_func():
# #         print("its a decor")
# #         func()
# #     return inner_func
# #
# #
# # @decorate_me
# # def ordinary():
# #     print("ordinary")
# #
# # #ordinary= decorate_me(ordinary)
# # ordinary()
# #
#
# def upper(func):
#     def inner_fun(messg):
#         return func(messg).upper()
#     return inner_fun
#
# #@echo
# def echo(messg):
#     return messg
#
# echo= upper(echo)
# print(echo("Hello"))


def div(a,b):
    print(a/b)


def smart_div(func):
    def inner_div(a,b):
        if a<b:
            a,b=b,a
            return func(a,b)
    return inner_div

div=smart_div(div)
div(2,4)
