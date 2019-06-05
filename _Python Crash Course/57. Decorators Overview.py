'''
Decorator - decorates your functions by adding addtional functionality.
decorates are used as on and off switches applying functionality that you may need once in a while, but not all the time
'''

# def hello(name='Nesta'):
#     print('the hello() func has been ran')
#
#     def greet():
#         return '    This is inside the greet()'
#
#     def welcome():
#         return '    This is inside welcome()'
#
#     # print(greet())
#     # print(welcome())
#
#     if name == 'Nesta':
#         return greet
#     else:
#         return welcome
#
# x = hello(name='sammy')
# print(x())


# def hello():
#     return 'Hi Nesta'
#
# def other(func): # <-- this took in the hello function above because we pass it at the bottom
#     print('Some other code')
#     # Assume that func passed in is a function!!!
#     print(func()) # prints out Hi "Hi Nesta" after "Some other code"
#
# other(hello) #<-- this took in the hello function above



def new_decorator(func):

    def wrap_func():
        print('some code before executing func')

        func()

        print('Code here, after executing func()')

    return wrap_func

@new_decorator # same as line 54. The @ represents a decorator method so you can remove line 54
def func_needs_decorator():
    print('Please decorate me!!') # This is printed second because its called below

# func_needs_decorator = new_decorator(func_needs_decorator) # This called the above to print second
func_needs_decorator()
