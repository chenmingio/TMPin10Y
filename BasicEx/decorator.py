import time

# def logger(msg):
#
#     def log_message():
#         print('Log:', msg)
#     return log_message
#
#
# log_hi = logger('Hi')
#
# log_hi()


# def html_tag(tag):
#
#     def wrap_text(msg):
#         print(f'{tag} and {msg}')
#
#     return wrap_text
#
#
# print_h1 = html_tag('h1')
# print_h1('foobar')

#
# def outside_function(func):
#     def inside_function(argv):
#         print(f'{func.__name__} is running with argument {argv}')
#     return inside_function

# def explainer(func, argv):
#     result = func()
#     print(f'The result of [.{func.__name__}()] is ==> {result}')
#
#
# explainer(time.time, None)

# def add(x, y):
#     add.__name__ = 'mulit'
#     return x*y
#
#
# result = add(5, 6)
# print(result)
# print(add.__name__)

#
# add_explainer = outside_function(add)
# add_explainer('string')


# explainer(add)


# def decorator_function(original_function):
#     def wrapper_function():
#         return original_function()
#     return wrapper_function
#
#
# display = decorator_function(display )


def explainer(orig_func):

    def wrapper(*args, **kwargs):
        result = orig_func(*args, **kwargs)
        print(f'{orig_func.__name__} result is ===> {result}')
        return result

    return wrapper


f = explainer(time.time)
f()
#
# @explainer
# def ptime():
#     return time.time()


# ptime()
