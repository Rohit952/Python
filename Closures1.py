# def func1():
#     def func2():
#         print("inside function 2")
#     func2()
# func1()     # inside function 2


#################################

# def func1():
#     def func2():
#         print("inside function 2")
#     return func2
# func1() # it won't print anything since u r not invoking inner func2().
# a = func1()
# print(a)        #  <function func1.<locals>.func2 at 0x0000023521A5BB70>
# a()     #  inside function 2 ..(it will be like func2())

######################################

# def greet_by_name(name):
#     def hello():
#         print('Hello ', name)
#
#     hello()
#     return hello
#
#
# a = greet_by_name("chris")  # Hello chris
# print(a)        #  <function greet_by_name.<locals>.hello at 0x0000029070FABB70>
# a()     #  Hello  chris

#########################################


# import random
#
# def greet_message(name, message):
#     annotations = ['+','*']
#     annotate = random.choice(annotations)
#
#     def greeting():
#         print(annotate * 50)
#         print(message, name)
#         print(annotate * 50)
#     return greeting()
# greet_message('ron','hello')

# or

# import random
#
# def greet_message(name, message):
#     annotations = ['+','*']
#     annotate = random.choice(annotations)
#
#     def greeting():
#         print(annotate * 50)
#         print(message, name)
#         print(annotate * 50)
#     return greeting
# a = greet_message('ron','hello')
# a()


############################################

# def enroll(col_name):
#     s_list =[]
#
#     def enroll_student(student_name):
#         s_list.append(student_name)
#         # print('Student name', student_name, 'has enrolled in', col_name)
#         print(f'student name {student_name} has enrolled in {col_name}')
#         print('Current student ', s_list, end = "\n")
#     return enroll_student
#
# enrol_yale = enroll('yale')
# enrol_yale('Sam')

a = [1,3,5,7]
b= [2,4,6,8,9]
# c = len(a)
# d = len(b)
l = []
def fun():
    for i in range(len(a or b)):
        l.append(a[i])
        l.append(b[i])
fun()
print(l)

