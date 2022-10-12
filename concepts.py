print("key concept of python")
"""
1.Print function
2. Escape characters
3. Mathematical or Arithmetic Operators
4. Relational operators or Conditional operators
5. Boolean variables
6. Conditional Statements
7. input function
8. Datastructures : List, tuple, set, dictionary
9. String functions
10.Concatenation operator
11. Loops : while, for, do while
12. Modules

"""

# print function
# () - parenthesis or round brackets

# print is a pre defined or pre built function
# print("Hello")
# print('hello world')


# escape characters:
# 3 types
# 1. \ - to escape from ' or ""
# 2. \n - for new line
# 3. \t - for tab space

# print("this is guddu's laptop")
# print("this is guddu \"s laptop")

# print('guddu\'s book')

# print("first line")
# print("second line")

# print("first line\nsecond line")
# print("first line\tsecond line")

# mathematical or arithmetic operators
# operators : +,-,*,/

# a+b - a and b are operands and + is operator

# print(2+3) # + is addition operator & 2 and 3 are operands
# print(2-3) # - is operator & 2 and 3 are operands
# print(2*3) # * is operator & 2 and 3 are operands
# print(10/2) # / is float quotient
# print(10//2) # // is integer quotient
# print(10%2) # % modulus or mod operator which gives us remainder

# student progress card

import turtle
name = "Biswo"
rollno = 102  # rollno is integer variable, and 102 is integer number
# percentage = 90.3

# print("Hello")
# print(name)

# print("Hello",name)

name1 = "Bill"
# print(name1)
# 3name = "Jack"

_name = "Jack Dorsey"
# print(_name)


# a  = 2
# print(a)
# a =3
# print(a)
# rules of variables
# 1. can have the combi of letters and numbers but it always should begin with either a characte or _

# 2. not supposed to use keywords

# 3 not supposed to give spaces in the variable

# print =2
# print(print)

# nameOfTheStudent = "Steve JObs"
# name_of_the_student = "Steve JObs"


# relational operators or conditional operators
# 1. >
# eg : 2 > 3 - Flase
# 2. <
# eg : 3<4 - True
# 3. >=
# eg : 3>=4 - False
# 3>=3 - True

# 4. <=
# eg : 2<=2 - True
# 3<=2 - False

# 5. == equals to operators
# 2==2 - True
# 2=="2" - False

# 6.!= not equal to
# 2!=2 -- False
# 3!=5 -- True

# NOte :
# 1. every number or symbol can be a string
# Eg :
# 2 - int
# '2' - string


# 2. but not every string can be number

# '2' -- string
# 2 - int

# 'A' - string
# we cant convert 'A' STRING INTO A NUMBER


# NOTE :
# = --> assignment operators
# b = 3


# a = 2
# b = 3
# print(a>b)
# print(a<b)
# print(a>=b)
# print(a<=b)
# print(a==b)
# print(a!=b)


# Boolean variables

# True or False in python
# true or false in javascript
# 1 or 0 in C program


# is_raining = False
# print(is_raining)


# conditional statement
# if
# if else
# elif

holiday = True
# if holiday:
#   print("I will buy you an Ice cream")
# else:
#   print("I will not buy Icecream because your school has no holiday")

# another example
# if 10>9:
#   print("10 is greater than 9")
# else:
#   print("10 is less than 9")


# print(10>9)

# logical operators
# 1. and
# 2. or

# if today is holiday and you are healthy then only i will buy icecream

# stm1 = today is holiday True
# stm2 = you are healthy  False
# result = i will buy Icecream

# find the biggest number among three numbers
# a = 2
# b = 4
# c = 3

# if a> b and a>c:
#   print("a is bigger than b and c")
# elif b>a and b>c:
#   print("b is greater than a and c")
# else:
#   print("c is greater than a. and b")


# finding the datatype of the variable
# using type() function

# a = 1
# b = 3.4
# c = "A"
# d = True
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))


# addition program
# a = 5
# b = 3
# print("addition",a+b)

# input function: input() allows to take input from keyboard
# note : by default input() always considers the input as string
# name = input("what is your name : ")
# print("Hello",name)
# print(type(name))


# a = input("enter your first number : ")
# b = input("enter your second number : ")
# print(type(a))
# print(type(b))
# # converting string into integer - type conversion
# # using int()
# a = int(a)
# b = int(b)
# print("after type conversion")
# print(type(a))
# print(type(b))


# print(a+b)

# even odd program
n = input("Enter your number: ")
n = int(n)


# Conditional statements
# is_raining = False
# if(is_raining):
#   print("I won't go out today")
# else:
#   print("I am going out today")

# conditional statements with Relational operators

# if(2>3):
#   print("2 is greater than 3")
# else:
#   print("2 is less than 3")

# if(5<=3):
#   print("2 is less than 3")
# else:
#   print("2 is greater than 3")

# type : a predefined we use to find the datatype of the variable
# computers = 95
# percentage = 95.6
# name = "Ivin"

# print("The data type of computers is ",type(computers))
# print("The data type of grade is ",type(percentage))
# print("The data type of name is ",type(name))

# input function : to take input from the keyboard
# input function always treats the input as string data type by default

# a = int(input("What is your number1 ? "))
# b = int(input("What is your number2 ? "))
# print(type(a))
# print(type(b))
# print(a+b)


# datastructures = structing or organising the data

# list
# tuple
# set
# dictionary

# string function
# group of characters
# len() - to find the length of the string
# upper() - to convert string into upper case
# lower() - to convert string into lower case

# name = "steve"
# # len(variable)
# print(len(name))
# # upper and lower
# #Syntax :  .upper() and .lower()
# print(name.upper())
# print(name.lower())

# concatenation operator : +
# print("Hi",name)
# to connect 2 str variables or a str variable and a string
# print("hello "+name)
# print("2"+3)

# fname="Ivin"
# sname = "Software Engineer"
# print(fname+ " " +sname)

# string slicing
# name = "Software"

# accessing a string character with index number - []
# print(name[2])
# print(name[2:6])

# print(name[3:5])
# 3 is inclusive and 5 is exclusive
# print(name[-2])
# reverse a string [::-stepnumber]
# print(name[::-1])
# print(name[::-2])

# List

# Collection of different data value.
# NOTE: the data type of the elements can be any data type

# sd = ["Ivin",101,98.5]
# print(sd)
# print("The name of student is ",sd[0])

# print(sd[0:2])

# functions in list
# sd.append(122)
# print(sd)
# # list.insert(index,element)
# sd.insert(1,95)
# print(sd)

# del keyword - to del whole list or a particular element in a list using index no

# del sd[2]
# print(sd)

# del sd
# print(sd)

# remove() : to remove a element by its value
# sd.remove("Ivin")
# print(sd)

# NOTE: LISTS ARE MUTABLE WHICH MEANS YOU CAN ALTER OR MODIFY THE ELEMENTS

# tuple - immutable which means you cannot alter or modify
# a tuple

# user1 = ("ivin@gmail.com","password")
# () - parenthesis
# user2 = ("steve@gmail.com")
# user1.append("kerla")
# print(user1[1])
# user1.remove("password")

# mergin tuples
# result = user1+user2
# print(result)

# common functions on both list and tuple
# len()

# print(len(user1))
# count() - to find the index no of an element
# sd = ["Ivin",101,98.5]
# print(sd.count(101))

# set : collection of unique objects
a = {1, 2, 3, 4, 4}
# print(a)
# union() or  | - bar or pipe

b = {4, 5, 6, 7}
# print(a|b)
# print(a.union(b))

# intersection() or & ampersand
# print(a&b)
# print(a.intersection(b))

# dictionary : collection of data value in the form of keys and values

# sd = {
#   "name":"Ivin",
#   "place":"Kerala",
#   "id":102,
#   # 1 : 90111,

# }

# print(sd.keys())
# print(sd.values())
# print(sd.items())

# print(sd["name"])
# print(sd[1])
# get function:
# to get the value of the key.
# print(sd.get("place"))
# print(sd.get("name"))


# print(sd)

# n = input("Enter anything")
# try:
#     n = int(n)
#     print(n, "is integer number")
# except ValueError:
#     try:
#         n = float(n)
#         print(n, "is float number")
#     except ValueError:
#         print(n, "is a string")


# loops
# while loop

# while(condition):
#   statements
#   inc or dec

# print 1 to 10 numbers
# n = 1
# while(n<11):
#   print(2*n)
#   # n = n+1
#   n += 3 # n = n+3

# 2 * 3 = 6
# 2 and 3 are factors
# 6 is the product

# factor : if a%n==0,then n is a factor
# a and b E Z


# print elements of a list using for loop
# sd = ["Ivin","Kerala",91004567893]
# for detail in sd:
#   print(detail)

# second way
# printing 10 numbers
# another way of using for loop - range() function
# syntax : for var in range(starting_no,ending_no(exclusive),step_no)
# for n in range(1,11):
#   print(n)

# for n in range(1,11,2):
#   print(n)


# table
# print 2 table
# 1. get 1 to 10 number using a loop
# 2. take a table_no var
# 3. multiply

# n = 1
# table_no = 2
# while(n<=10):
#   print(2 ,"*", n, "=", (2*n))
#   n+=1

# n = 1
# while(n<11):
#   print(n)
#   n*=2

sd = {
    "name": "Ivin",
    "Id": 101,
    "Place": "Kerala"
}
# print(sd.keys()) #to print all keys
# print(sd.values()) # to print all values
# print(sd.items()) # to print as pairs
# print(sd["Id"])

# for loop in dictionary
# for k in sd:
#   print("key is",k)
#   print("value is ", sd[k])


# for n in sd.keys():
#   print(n)

# for n in sd.values():
#   print(n)

# for n in sd.items():
#   print(n)


# 5

# no_of_factors = 0
# for(4)
# 1 - yes
# no_of_factors += 1 #1
# 2 - yes
# no_of_factors += 1 #2
# 3-no
# 4 - yes
# no_of_factors += 1 #3

# if(no_of_factors > 2):
#   not prime

# prime no : if number of factors > 2


# loop : sequential exec
# function : random execu
# pre defined functions:
# input,print,int,list,float,choice....

# user defined function
# syntax :

# there are two main parts in a function
# 1. function definition
# 2. function calling

# 1. function definition

# def functionname (formal parameters):
#   statements...


# 2. function calling
# functionname(actual parameters)

# formal parameters : the parameters which are received from function calling

# actual parameters ; the parameters you send


# a = int(input("number 1 : "))
# b = int(input("number 2 : "))
# print(a+b)

# def addition(a,b):
#   print(a+b)


# addition(2,4)
# addition(5,4)
# addition(6,4)
# addition(2,7)


# # return
# # bal_enq

# def bal_enq(password):
#   if password == "123":
#     return 5000
#   else:
#     return "Don't waster your time"

# receipt = bal_enq("123")
# print(receipt)

# print(bal_enq("123"))

# 2 and 4 are actual parameters


# print nth table_no

# def mul_table(n):
#   for i in range(1,11):
#     print(n , "*" , i , "=", n*i)


# table = int(input("Enter a number : "))
# mul_table(table)


# def factors(n):
#   nf = 0
#   for i in range(1,n+1):
#     if n%i==0:
#       nf+=1

#   print(nf)

# factors(4)

# is_raining = False
# if(is_raining):
#   print("it is raining here")
# else:
#   print("it is not raining here")

# random
# import random
# # import math

# s_list = ["Steve","Bill","Elon"]

# result = random.choice(s_list)
# print(result)
# # generating a random integer number
# n = random.randint(1,5)
# note : randint parameters are inclusive which means here, 1 and 5 are inclusive
# print(n)
# import math
# # math library
# print(int(math.sqrt(16)))

# pow(base,exponent)
# print(math.pow(2,3))


ball = turtle.Turtle()
# forward()
# backward()
# forward and backward - distance

# left()
# right()
# left and right are for angles

# ball.forward(100)
# ball.right(90)
# ball.forward(100)
# ball.right(90)
# ball.forward(100)
# ball.right(90)
# ball.forward(100)
# ball.right(90)

# for i in range(4):
#   ball.forward(100)
#   ball.right(90)

# name = "sTeVe"
# print(name[0].upper() + name[1:].lower())


# def multi(a,b):
#   print(a*b)

# multi(2,3)

# ctrl + /
# name = "steve"
# name = list(name)
# name[3] = "z"
# print(name[3])
# print(name)

# answer = "_ "*len(name)
# print(len(answer))

Melon ASSIGNMENT - PYTHON

1. There are two friends Shubham and Trinadh. One Day, they want to buy Watermelon. they both collectively bought a watermelon and ready to share.
Conditions:
1. Shubham and Trinadh love even numbers only, so if the part is an odd number they won't take it.
Eg:
1.if WATERMELON is 6 kgs, then each one will get 3 kilos. ANSWER SHOULD BE "WE DON'T WANT THIS"
2. If the watermelon is 8 kgs, then each one will get 4 kilos and the answer should be "Lets Share"
