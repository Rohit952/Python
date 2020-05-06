# Closures are an important constructs used in Python Decorators

# Decorators :- It helps in adding functionality to existing codes without modifying code itself.

# import random
#
# def decorators():
#     print("Decorators are Cool")
#
# def highlighter():
#
#     annotations = ['+', '*']
#     annotate = random.choice(annotations)
#
#     print(annotate * 50)
#     decorators()
#     print(annotate * 50)
# highlighter()

##################################################
# import random
#
#
# def decorators():
#     print("Decorators are Cool")
#
#
# def another():
#     print('Decorators use Closures')
#
#
# def make_highlighter(func):
#     annotations = ['+', '*']
#     annotate = random.choice(annotations)
#
#     def highlight():
#         print(annotate * 50)
#         func()
#         print(annotate * 50)
#
#     return highlight()
#
#
# # another = make_highlighter(another)
# @make_highlighter
# def three():
#     print('three')


###################################################

# def asterik_highlight(func):
#     def highlight():
#         print('*' * 50)
#
#         func()
#
#         print('*' * 50)
#
#     return highlight
#
#
# @asterik_highlight
# def func1():
#     print('1st Decorator')
#
#
# func1()

#########################################################

# def asterik_highlight(func):
#     def highlight():
#         print('*' * 50)
#
#         func()
#
#         print('*' * 50)
#
#     return highlight

# def plus_highlight(func):
#     def highlight():
#         print('+' * 50)
#
#         func()
#
#         print('+' * 50)
#
#     return highlight
#
# @plus_highlight
# @asterik_highlight
# def func1():
#     print('1st Decorator')
# func1()

################################################
