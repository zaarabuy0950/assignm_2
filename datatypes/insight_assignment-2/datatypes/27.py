def decorator_function(main_function):
    def inner_function(*args,**kwargs):
        print('i m a developer')
        return main_function(*args,**kwargs)
    return inner_function

# @decorator_function
def display(msg):
    print(msg)


display=decorator_function(display)
display('hello,whats up')
