# Method overloading: allowing different parameters for calling the same method

# No direct Method Overloading in python but achievable using multipledispatch module.

# def add(a,b):
#     return a+b
# def add(a,b,c):
#     return a+b+c
# add(2,3)


# Method overriding: overwriting the functionality of a method defined in a parent class.

# class A():          # Method Overriding
#     def hello(self):
#         print("From A")
# class B(A):
#     def hello(self):
#         print("From B")
# b = B()
# b.hello()

########################################################

# a = [5,6,77,45,22,12,24]
# b = [i for i in a if i % 2 != 0]
# print(b)

# a = [5,6,77,45,22,12,24]
# b = []
# for i in a:
#     if i %2 != 0:
#         b.append(i)
# print(b)

# a = [5,6,77,45,22,12,24]
# print(list(filter(lambda x : x%2 != 0,a)))

# def even(n):
#     return n %2 != 0
# a = [5,6,77,45,22,12,24]
# print(list(filter(even,a)))

##################################################################


# performance decorator.
# from time import time
# def performance(fn):
#   def wrapper(*args, **kwargs):
#     t1 = time()
#     result = fn(*args, **kwargs)
#     t2 = time()
#     print(f'took {t2-t1}')
#     return result
#   return wrapper
#
# @performance
# def long_time():
#     for i in range(10000):
#         i*5
#
# long_time()

###########################################################


# name = 'Cindy'
# amount = 50
# print(f"Hello {name}, your balance is {amount}.")

#########################################################


# Syntax of lambda Function:

# lambda argument_list : expression


# s=lambda n:n*n
# print("The Square of 4 is :",s(4))
# print("The Square of 5 is :",s(5))


# lst=[0,5,10,15,20,25,30]
# l1=list(filter(lambda x:x%2==0,lst))
# print(l1) #[0,10,20,30]
# l2=list(filter(lambda x:x%2!=0,lst))
# print(l2) #[5,15,25]


# l=[1,2,3,4,5]
# l1=list(map(lambda x:x*x,l))
# print(l1) #[1, 4, 9, 16, 25]


# from functools import reduce
# l=[10,20,30,40,50]
# result=reduce(lambda x,y:x+y,l)
# print(result) # 150

#################################################################

# a = eval(input("enter a list of numbers : "))     # [10,20,33]
# count = 0
# c = [i for i in a if i%2 == 0]
# print(c)      # [10,20]
# print(len(c))     # 2

#################################################################


# s="This is New York"
# lic = [i[::-1] for i in s.split()]
# print(' '.join(lic))   #   sihT si weN kroY

# print(s[::-1])      #  kroY weN si sihT


# or

# s = input("enter a string : ")      #  this is new york
# a = s.split()
# l1 = []
# for i in a:
#     l1.append(i[::-1])
# output = " ".join(l1)
# print(output)       # siht si wen kroy

############################################################


# s="This is New York"
# b=s.split()
# c = b[::-1]
# print(c)        #  ['York', 'New', 'is', 'This']
# print(" ".join(c))  # York New is This

##############################################################


# a = ["durga", "soft", "solutions"]
# print(':'.join(a))  # durga:soft:solutions  (list or tuple)


# b = "Hello world! my first program"
# print(b.startswith("Hello"))  # True
# print(b.endswith("program"))    # True


# a = 'CatBatSatFatOr'
# n=3
# for i in range(0,len(a),n):
#     print(a[i:i+n],end=" ")         # Cat Bat Sat Fat Or


# txt = "hello, my name is Peter, I am 26 years old"
# x = txt.split(", ")
# print(x)      #  ['hello', 'my name is Peter', 'I am 26 years old']

# word = 'geeks, for, geeks, pawan'
#
# # maxsplit: 0
# print(word.split(', ', 0))      # ['geeks, for, geeks, pawan']
# print(word.split(', ', 4))      # ['geeks', 'for', 'geeks', 'pawan']
# print(word.split(', ', 1))      # ['geeks', 'for, geeks, pawan']

###########################################################################


# str1 = input("Please enter your own String : ")
# ch = input("Please enter your own Character : ")
#
# count = 0
# for i in range(len(str1)):
#     if str1[i] == ch:
#         count += 1
#         print(ch, "is found at index position : ", i + 1)
# print("Total count is :", count)

################################################################
#  The find() method returns the lowest index of the substring
#  if it is found in given string. If its not found then it returns -1.

""" rfind() method returns the highest index of the substring
    if found in given string. If not found then it returns -1.

Syntax :
str.rfind(sub, start, end)"""

"""count() function is an inbuilt function in python programming
   language that returns the number of occurrences of a substring 
   in the given string.

Syntax:

string.count(substring, start=…, end=…)"""

# string = "geeks for geeks"
# print(string.count("geeks"))     # 2
# print(string.count("geeks", 0, 5))  # 1

##################################################################

# Python find Method Example

# a = "Welcome to Python Programming Language"
# print(a.find("Python"))     # 11
# print(a.rfind("to", 2,11))      # 8


# Str1 = 'We are abc working at abc company'
# Str2 = Str1.find('abc')
# print('First Output of a find() method is = ', Str2)        # 7
#
# # Performing find() function directly
# Str3 = 'Find Tutorial at Tutorial Gateway'.find('Tutorial')
# print(Str3)     # 5
#
# # Searching for Not existing Item
# Str4 = Str1.find('Tutorial')
# print(Str4)     # -1
#
# # Using First Index while finding the String
# Str5 = Str1.find('abc', 12)
# print(Str5)     # 22
#
# # Using First & Second Index while finding the String
# Str6 = Str1.find('abc', 12, len(Str1) -1)
# print(Str6)     # 22
#
# # Using First & Second Index while finding Non existing String
# Str7 = Str1.find('abc', 12, 21)
# print(Str7)         # -1

#####################################################################

# print(eval("10+24-36*100"))  # -3566
# print(eval("5/4*100-2"))    #123.0


# a = eval(input("Enter a list of numbers : "))
# print(a)      # [10,20.5,"hello"]    [10,20.5,'hello']


# a = eval(input("Enter a string : "))
# for i in range(len(a)):
#     print("The letter {} is present at positive index position {} or at negative index {}".format(a[i],i,i-len(a)))

# or

# a = eval(input("Enter a string : "))
# i= 0
# for x in a:
#     print("The letter {} is present at index position {} or at negative index {}".format(x,i,i-len(a)))
#     i+=1

##########################################################################


# num = eval(input("Enter a number in between 1 to 100 : "))
# if num >= 1 and num <=100:
#     print("%i exists in between %i and %i" %(num,1,100))
# else:
#     print("{} doesn't exist in between {} and {}".format(num,1,100))

##########################################################################


# Decimal to Binary Conversion
# print(bin(10).replace('0b',""))
# print(bin(10)[2:])


# a = int(input())
# b=bin(a)
# z= format(a,"b")
# print(z)

####################################################


# sr = input()        # This is Rohit
# n = sr.split()
# for i in n:
#     if len(i)>3:
#         print(i[0] + i[1:len(i)-1][::-1] + i[-1], end=" ")
#     else:
#         print(i,end=" ")        #  Tihs is Rihot

####################################################

# binary = input('enter a number: ')
# decimal = 0
# for digit in binary:
#     decimal = decimal*2 + int(digit)
# print(decimal)

####################################################


# n=int(input())
# for i in range(1,n+1):
#     print("* "*i)

# n=int(input())
# for i in range(0,n):
#     print(("* ")*(n-i))

# n=int(input())
# for i in range(0,n):
#     print((" "*(i)+("* ")*(n-i)))

###################################################
# Palindrome Number

# a = input()
# print("Palindrome" if a==a[::-1] else "Not a Palindrome")


####################################################


# print("Enter 1 for number or 2 for string")
# i=int(input())
# while i==1:
#     print("Enter a number to check for palindrome : ")
#     a = int(input())
#     b= str(a)
#     c= b[::-1]
#     if int(c)==a:
#         print("it is a palindrome")
#     else:
#         print("not a palindrome")
#         break
# else:
#     c = str(input("Enter a character :"))
#     d = c[::-1]
#     if d==c:
#         print("Enter string is a palindrome")
#     else:
#         print("Not a palindrome")

##########################################################

# fact = 1
# a = int(input("enter a number : "))
# if a < 0:
#     print("factorial does not exist for negative numbers")
# elif a == 0:
#     print("factorial is : 1")
# else:
#     for i in range(1, a+1):
#         fact = fact*i
#     print("factorial of " + str(a) + " is :",fact)
#     print("factorial of {} is : {}".format(a,fact))
#     print("factorial of {} is :".format(a),fact)

###########################################################

# def factorial(num):
#
#     fact = 1
#     if num < 0:
#         print("factorial does not exist for negative numbers")
#     elif num == 0:
#         print("factorial is : 1")
#     else:
#         for i in range(1, num+1):
#             fact = fact*i
#         print("factorial of " + str(num) + " is : ", fact)
#
# factorial(int(input("enter a number : ")))

################################################################

# Program to ask the user for a range and display all Armstrong numbers in that interval

# lower = int(input("Enter lower range: "))
# upper = int(input("Enter upper range: "))
# for num in range(lower, upper + 1):
#     sum = 0
#     temp = num
#     while temp > 0:
#         digit = temp % 10
#         sum += digit ** 3
#         temp //= 10
#     if num == sum:
#         print(num)    
# else:
#     print("no armstrong numbers")
        

########################################################

# number = int(input("Please enter a number: "))
#
# num_str = str(number)
# num_len = len(num_str)
#
# sum_of_digits = 0
# for d in num_str:
#     sum_of_digits += int(d) ** num_len  # power operation
#
# if number == sum_of_digits:
#     print("{} is an Armstrong number of order {}".format(number, num_len))
# else:
#     print("{} is NOT an Armstrong number".format(number))

###########################################################

# num = int(input("enter a number: "))
#
# length = len(str(num))
# sum = 0
# temp = num
#
# while (temp != 0):
#     rem = temp % 10
#     sum = sum + (rem ** length)
#     temp = temp // 10
#
# if sum == num:
#     print("armstrong number")
# else:
#     print("not armstrong number")

##########################################################

# b_num = list(input("Input a binary number: "))
# value = 0
#
# for i in range(len(b_num)):
#     digit = b_num.pop()
#     if digit == '1':
#         value = value + pow(2, i)
# print("The decimal value of the number is", value)

#########################################################

# import math
#
# a = int(input("enter a number : "))
# b = int(input("enter a number : "))
# print("GCD of {} and {} is".format(a,b),math.gcd(a,b))

#########################################################

# def gcd(a,b):
#     if b==0:
#         return a
#     else:
#         return gcd(b,a%b)
# a=int(input("Enter a number : " ))
# b=int(input("Enter another number : "))
# print("gcd of {} and {} is ".format(a,b), gcd(a,b))

##########################################################
#
# def gcd(a,b):
#     if b==0:
#         return a
#     else:
#         return gcd(b,a%b)
# a=int(input("Enter a number : " ))
# b=int(input("Enter another number : "))
# print("gcd of {} and {} is".format(a,b), gcd(a,b))
#
# lcm = (a*b)/gcd(a,b)
# print("lcm of {} and {} is".format(a,b), lcm)

##########################################################

"Decimal to other type Conversion"

# a = 15
# print("binary is : ", bin(a))
# print("binary is :", format(a,"b"))
# print("octal is : ", oct(a))
# print("hexadecimal is : ", hex(a))

"Binary to other type Conversion"

# b = "1111"
# c = int(b,2)
# print("decimal is : ", int(b,2))
# print ("octal is is : ", oct(c))
# print ("hexadecimal is is : ", hex(c))

"octal to other type Conversion"

# a = "17"
# b = int(a, 8)
# print("Decimal is : ", int(a, 8))
# print("Binary is : ", bin(int(a)))
# print("Hexadecimal is : ", hex(b))

"Hexadecimal to other type Conversion"

# a= "F"
# b = int(a,16)
# print("Decimal is : ", int(a, 16))
# print("Binary is : ", bin(b))
# print("octal is : ", oct(b))

###############################################################

# sum of all elements in a list


# from functools import reduce
# print(reduce(lambda x,y: x+y, [5,4,2,10,-2,-3]))

# a = [5,4,2,10,-2,-3]
# total = 0
# i = 0
# for i in range(len(a)):
#     total += a[i]
# print(total)

# or

# a = eval(input("Enter a list of any numbers : "))
# total = 0
# for i in range(len(a)):
#     total += a[i]
# print(total)

# or

# a = eval(input("Enter a list of any numbers : "))
# total = 0
# for i in a:
#     total += i
# print(total)

# or

# a = eval(input("Enter a list of numbers : "))
# i,total = 0,0
# while i<= len(a)-1:
#     total += a[i]
#     i += 1
# print(total)

# or

# a = eval(input("Enter a list of numbers : "))
# total = 0
# i = 0
# while a[i] in a:
#     total += a[i]
#     if i == len(a)-1:
#         break
#     i += 1
# print(total)


##############################################################
# Sorting of a list and sum of only positive numbers of a list

# a = [5,4,2,10,-2,-3]
# total = 0
# i = 0
# a.sort(reverse=True) # descending order list sort
# print(a)
# while a[i]>0:
#     total += a[i]
#     i +=1
# print(total)

# or

# a = eval(input("Enter a list of both +ve and _ve numbers : "))
# a.sort(reverse = True)
# i,total = 0,0
# for i in range(len(a)):
#     if a[i]>0:
#         total += a[i]
# print(total)

# or

# a = eval(input("Enter a list of both +ve and _ve numbers : "))
# a.sort(reverse = True)
# total = 0
# for i in a:
#     if i > 0:
#         total += i
# print(total)

################################################################

# # take second element for sort
# def takeSecond(elem):
#     return elem[1]

# random = [(2, 2), (3, 4), (4, 1), (1, 3)]

# # sort list with key
# random.sort(key=takeSecond)
# print('Sorted list:', random)

# or

# random = [(2, 2), (3, 4), (4, 1), (1, 3)]
# print('Sorted list:', sorted(random, key=lambda x:x[0]))  


# random = [(2, 2), (3, 4), (4, 1), (1, 3)]
# random.sort(key=lambda x:x[0])
# print('Sorted list:', random)

################################################################

# list Comprehensions

# line = ["hello","world"]
# a = [i[0] for i in line]
# print(a)    # ['h', 'w']

# or


# line = ["hello", "world"]
# a = []
# for i in line:
#     a.append(i[0])
# print(a) # ['h', 'w']


# line = "I like to play guitar and piano and drums"
# words = line.split()
# letters = [word[0] for word in words]
# print ("".join(letters))   #Iltpgapad

# a,b = [int(x) for x in input("enter 2 values : ").split()]
# print(a,b)    # run time 20 30  output 20 30

# a,b = [float(x) for x in input("enter 2 values : ").split(',')]
# print(a,b)    # 20,30   20.0 30.0

# a,b,c,d = [int(x) for x in input("enter 4 values : ").split(':')]
# print(a*b*c*d)

# a,b,c = [eval(x) for x in input("enter 3 values of different data types : ").split(',')]
# print(a,b,c)  # 10,20.5,"hello"    10 20.5 hello

# a = []
# for x in range(10):
#     if x % 3 == 0:
#         a.append(x)
# print(a)            # [0,3,6,9]


# a = [x for x in range(int(10)) if x % 3 == 0]
# print(a)        # [0, 3, 6, 9]


# a = [2,4,6,8,10]
# d = [x*2 for x in a]
# print(d)

# or

# a = [2,4,6,8,10]
# print(list(map(lambda x:x*2,a)))

# or

# a = [2,4,6,8,10]
# c=[]
# for x in a:
#     c.append(x*2)
# print(c)        # [4, 8, 12, 16, 20]

#################################################

# a = [x**2 for x in range(1,7)]
# print(a)
# a.sort(reverse = True)
# print(a)      # [36,25,16,9,4,1]

# a = [x**2 for x in range(6,0,-1)]
# print(a)      # [36,25,16,9,4,1]

# c = []
# for x in range(6,0,-1):
#     c.append(x**2)
# print(c)        # [36, 25, 16, 9, 4, 1]

###############################################

# a = "The"
# for i in range(len(a)):
#     c = a[i]*2
#     print(c,end="")     # TThhee


#################################################


# a = eval(input("enter a list of numbers : "))
# count = 0
# c = [i for i in a if i%2 == 0]
# print(c)
# print(len(c))       # [10,23,46]     [10,46]  2


# a = [1,3,5,4,6,7,8,12]
# count = 0
# for i in range(len(a)):
#     if a[i] % 2 == 0:
#         count += 1
# print(count)

# a = [1,3,5,4,6,7,8,12,18,646]
# i = 0
# count = 0
# while i < len(a):
#     if a[i] % 2 == 0:
#         count += 1
#     i +=1
# print(count)


# Python Program to Count Even and Odd Numbers in a List

# NumList = []
# Even_count = 0
# Odd_count = 0
#
# Number = int(input("Please enter the Total Number of List Elements: "))
# for i in range(1, Number + 1):
#     value = int(input("Please enter the Value of %d Element : " %i))
#     NumList.append(value)
#
# for j in range(Number):
#     if(NumList[j] % 2 == 0):
#         Even_count = Even_count + 1
#     else:
#         Odd_count = Odd_count + 1
#
# print("\nTotal Number of Even Numbers in this List =  ", Even_count)
# print("Total Number of Odd Numbers in this List = ", Odd_count)

# Python Program to Count Even and Odd Numbers in a List

# NumList = []
# Even_count = 0
# Odd_count = 0
# j = 0
#
# Number = int(input("Please enter the Total Number of List Elements: "))
# for i in range(1, Number + 1):
#     value = int(input("Please enter the Value of %d Element : " %i))
#     NumList.append(value)
#
# while(j < Number):
#     if(NumList[j] % 2 == 0):
#         Even_count = Even_count + 1
#     else:
#         Odd_count = Odd_count + 1
#     j = j + 1
#
# print("\nTotal Number of Even Numbers in this List =  ", Even_count)
# print("Total Number of Odd Numbers in this List = ", Odd_count)

##########################################################################

# Get a list of numbers as input from a user and Print it without using a split() function

# numberList = []
# n = int(input("Enter the list size : "))
# for i in range(0, n):
#     print("Enter number at location", i, ":")
#     item = int(input())
#     numberList.append(item)
# print("User List is ", numberList)

# or

# n = int(input("enter number of elements : "))
# a = []
# for i in range(n):
#     b = int(input("enter a number : "))
#     a.append(b)
# print(a)

# n = int(input("Enter the size of list : "))
# numList = list(int(num) for num in input("Enter the list numbers separated by space: ").strip().split())[:n]
# print("New List: ", numList)


#################################################

# a = str(input())
# c = ""
# for i in range(len(a)):
#     c += a[:i+1]
# print(c)    #  Code   CCoCodCode

##################################################

# a = 0
# b = 1
# total = 0
# print(a, end=" ")
# for i in range(9):
#     total = b + a
#     a = b
#     b = total
#     print(total, end=" ")
#
# a, b = 0, 1
# total = 0
# while True:
#     a,b = b, a + b
#     print(b, end=" ")
#     if b >= 4000000:
#         break
#     if b % 2 == 0:
#         total += b
# print(total)

########################################################

# N = int(input().strip())
#
# if N % 2 != 0:
#     print ("Weird")
# elif N >= 2 and N <= 5:
#     print ("Not Weird")
# elif N >= 6 and N <= 20:
#     print ("Weird")
# elif N > 20:
#     print ("Not Weird")


# n = int(input())
# if n % 2 == 1:
#     print("Weird")
# elif n % 2 == 0 and 2 <= n <= 5:
#     print("Not Weird")
# elif n % 2 == 0 and 6 <= n <= 20:
#     print("Weird")
# else:
#     print("Not Weird")

############################################
#
# year=int(input("Enter year to be checked:"))
# if(year%4==0 and year%100!=0 or year%400==0):
#     print("The year is a leap year!")
# else:
#     print("The year isn't a leap year!")
#
#
# def is_leap(year):
#     # leap = False
#     if(year%4==0 and year%100!=0 or year%400==0):
#         return True
#     else:
#         return False
#
# year = int(input())
# print(is_leap(year))


##########################################

# n = int(input("enter number of elements : "))
# a = []
# for i in range(n):
#     b = int(input("enter a number : "))
#     a.append(b)
# print(a)
# a.sort()
# print("2nd largest element is : ", a[-2])

# or

# a = eval(input("Enter a list of numbers : "))
# b=a.sort(reverse=True)
# print(a[1])

#####################################################

# with open("test.txt", 'w', encoding='utf-8') as f:
#     # f.write("my first file\n")
#     # f.write("This file\n\n")
#     # f.write("contains three lines\n")

#     f = open("test.txt", "a")
#     f.write("Hello World\n")
#     f.write("Hello World! Hey")
#     f.close()

######################################################

# a = list(range(1,21))
# print(a)                # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# print(a[1:])            # [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# print(a[:1])            # [1]
# print(a[::-1])          # [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# print(a[::-2])          # [20, 18, 16, 14, 12, 10, 8, 6, 4, 2]
# print(a[::-4])          # [20, 16, 12, 8, 4]
# print(a[2:-10:-1])      # []
# print(a[-1:-8:-1])      # [20, 19, 18, 17, 16, 15, 14]
# print(a[-2:10:-1])      # [19, 18, 17, 16, 15, 14, 13, 12]

#######################################
# Generate random 10 digit number

# import random
# a = [i for i in range(10)]
# b = '' + str(random.randint(7,9))
# for i in range(9):
#     b += str(random.choice(a))
# print(int(b))
# print(type(b))

#########################################

# import random

# def ph_gen():
#     d =  str(random.randint(7,9))
#     for i in range(9):
#         d += str(random.randrange(0,9))
#     return d

# a = ph_gen()
# print(a)

##############################################################################

# NumList = []

# Number = int(input("Please enter the Total Number of List Elements: "))
# for i in range(1, Number + 1):
#     value = int(input("Please enter the Value of %d Element : " %i))
#     NumList.append(value)

# for i in range (len(NumList)):
#     for j in range(i + 1, len(NumList)):
#         if(NumList[i] > NumList[j]):
#             NumList[i],NumList[j] = NumList[j],NumList[i]

# print("Element After Sorting List in Ascending Order is : ", NumList)

############################################################################


# s = []
# Number = int(input("Please enter the Total Number of List Elements: "))
# for i in range(1, Number + 1):
#     value = int(input("Please enter the Value of %d Element : " %i))
#     s.append(value)
# nl = []
# for i in range(len(s)):
#     a = min(s)
#     nl.append(a)
#     s.remove(a)

# print (nl)