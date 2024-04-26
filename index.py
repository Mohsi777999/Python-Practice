# Python Practice - 1

# print("My name is","Mohsin Ali","and my age is 19")
# print(40)

# name = "Mohsin"
# age = 19
# price = 20.7

# print(name)
# print(age)
# print(price)

# print("My name is",name)
# print("My age is",age)

# Type Function in python
# age = 25
# print(age)

# print(type(name))
# print(type(age))
# print(type(price))

# Boolean
# a1 = True
# a2 = None

# print(type(a1))
# print(type(a2))

# Arthimetic Operator
# num1 = 20
# num2 = 30
# sum = num1+num2
# print(sum)

# ab = "Mohsin"
# ba = "12"
# print(ab+ba)

# a,b = 2,3
# print(a,b+b)

# number1,number2 = 20,3.5
# result = number1+number2*number1
# print(result)

# no1,no2 = 10,2.5
# print(no1/no2)

# no1,no2 = 10,2.5
# print(no1//no2)

# numb = 10
# print(float(numb))


# num1, num2 = 10, 20
# print(num1 % num2)

# name = input("Name : ")
# print("My name is", name)

# num = int(input("Enter your phone number : "))
# print("Your number is : ", num)

# Conditional Statement in Python

# light = input("Light is : ")

# if light == "red":
#     print("Stop")
# elif light == "yellow":
#     print("Look")
# elif light == "green":
#     print("Go")
# else:
#     print("Light is broken")

# Grading System in Python

# marks = int(input("Enter your marks : "))

# if marks >= 80:
#     print("A-1 Grade")
# elif marks >= 70 and marks < 80:
#     print("A Grade")
# elif marks >= 60 and marks < 70:
#     print("B Grade")
# elif marks >= 50 and marks < 60:
#     print("C Grade")
# elif marks >= 40 and marks < 50:
#     print("D Grade")
# else:
#     print("Fail")

# Conditonal Statement in short syntax

# food = input("Food : ")
# eat = "Yes you can eat" if food == "cake" or food == "rice" or food == "banana" else "You can't eat"
# print(eat)

# food = input("Food : ")
# print("This is sweet") if food == "cake" or food == "jalebi" or food == "candy" else print("This is't sweet")

# Type Conversion in Python

# num1 = int("20")
# num1 = float("20")
# num1 = str("20")
# num2 = 20
# print(num1 + num2)

# Escape Sequence

# str1 = "Hi how are you\nnice to meet you iam your father"
# print(str1)
# str2 = "Hello\tWorld"
# print(str2)

# Concatenation

# str1 = "My name is "
# str2 = "Mohsin Ali"
# result = str1+str2
# print(result)
# Length fun
# print(len(str2))

# Indexing in python

# name = input("Enter your name : ")
# first = name[0]
# last = name[5]
# print("Your first character of name is", first, "and last character is", last)

# Slicing Most important topic in python
# Slicing is a topic that breaks string into pieces

# str = "Iam learning python"
# slice = str[13:19] result = python
# slice = str[13:] result = python . same
# slice = str[4:12]
# print(slice)

# Now Negative slicing index

# str = "Apple"
# slice = str[-3:]
# slice = str[-4:-1]
# slice = str[-5:-2]
# print(slice)

# prof = input("who are you :")
# state = "your profession ends with 'er' so you are authentic" if prof.endswith("er") else "your profession not ends with 'er' so you are not authentic"
# print(state)

# srt = "mohsin"
# result = srt.endswith("sin")
# print(result)

# num = int(input("Enter number :"))
# even = num % 2
# result = "This is even number" if even == 0 else "This odd number"
# print(result)

# num1 = 12
# num2 = 10
# num3 = 25

# if num1 > num2 and num1 > num3:
#     print(num1)
# elif num2 > num1 and num2 > num3:
#     print(num2)
# else:
#     print(num3)
