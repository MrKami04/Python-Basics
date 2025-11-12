print("Hello World!.")

# creating variable 
number = 45; print(number)
myName = "Python"; print(myName)

# other method to creating variabe :
number1 = int(222);  print(number1)
myAge = str(23); print(myAge)

# check type of variable of data: type() fuction
print(type(myAge))

# variable name are case-sensitive: both are different name
a = 12; print(a)
A = 15; print(A)

# there are many techniques to declare a variable name for more readability and clearity as :
# 01-technique: camel-Case as each word starting letter capital except first letter.
myName = "Python"; myVariableName = "John"; print(myName,"   ",  myVariableName) 

# 02-technique: Pascal-Case as each word start with capital letter.
MyVariableName = "John bro"; print(MyVariableName)

#  03-technique: snake-case as each word separate with underscore( _ ).
my_variable_name = "John-king";print(my_variable_name)

# multiple value assigne
x, y, z = 3, 4, 5; print(x, y, z)
a1 = b1 = c1 = "Hello!"; print(a1, b1, c1)

# number in python
numInt = 23; print(numInt); print(type(numInt))  # integer number
numFloat = 45.32; print(numFloat); print(type(numFloat)) # float number
numComplex = 2 + 23j; print(numComplex); print(type(numComplex)) # complex number
print(complex(numInt)) # type cooversion into complex but can't complex into int
print(complex(numFloat))  # type cooversion into complex but can't complex into float

# random number
import random
numRand = random.randrange(1, 10); print("random number :", numRand)

# string: 
a2 = "Hello"; print(a2); print(len(a2))
b2 = 'Hello'; print(b2); print(len(b2))
# check string is present or not
a3 = "Hello, i am python"; print('python' in a3); print("python" not in a3)
# string slocing
strSlice = "Hello, are doing slicing of string!";
print(strSlice[2:7]);print(strSlice[:4]) # from start
print(strSlice[2:]);print(strSlice[-5:-3]) # negative slicing

# modify string by upper(), lower(), strip() for remove whitespace, replace(), split() function
strModify = "     Pythn is the most popular, programming language today's.    "
print(strModify.upper());print(strModify.lower());print(strModify.strip())
print(strModify.replace('most', 'very most'));print(strModify.split(','))
# concate string by '+' operator use
str1 = 'hello'; str2 = 'world!'; print(str1 + " " + str2)
# format string
pub_python = 1991
auth_python = 'Guido van Rossum'
txt_py = f"python publish in {pub_python}"

txtpy1 = "python create in {} by {}".format(pub_python, auth_python)
print(txtpy1)
print(txt_py)
price = 555
txtPrice = f"the price of this pen is {price: .2f}$$"; print(txtPrice)
txtPrice = f"the price of this pen is $$"; print(txtPrice)

# boolean python
print(5>6);print(bool(666))
print(66 < 333);print(bool("hello"))
x = 200;print(isinstance(x, int))

# 01arithmatic operator are : +, -, *, /, //, *, %
x11 = 12; x22 = 5; print(x11 / x22); print(x11 // x22)

# 02 Assignment operators are: =, +=, -=, *=, /=, %=, //=, **=, &=, |=, ^=, >>=, <<=, :=(walrus operator)
## type lines, press Enter on empty line to stop
# while (line := input("line: ").strip()) != "":
#     print("You typed:", line)

## type lines, press Enter on empty line to stop
#line = input("line: ").strip()
# while line != "":
#     print("You typed:", line)
#     line = input("line: ").strip()

# 03comparison operator: ==, >, <, >=, <=, !=
print(5==5)

# 04logical operator: and, or, not, 
x33 = 34; print(x33 > 4 and x33 < 45)

print("----------")
# 05 Identity operator: is , is not
x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)
print(x is y)
print("---------")
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
print(x is y)
print(x == y)


# 06 membership operator: in , not in
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)
print("banana" not in fruits)

# 07 Bitwise operator: &(AND), |(NOR), ^(XOR), ~(NOT), <<(LEFT SHIFT), >>(RIGHT SHIFT)
print(6 & 3); print(6 | 3); print(6 ^ 3)

# list in python:
myList = ["apple", "banana", "cherry", "apple"];print(myList);print(len(myList))
# list take different data type
list1 = ["abc", 34, True, 40, "male"]; print(list1);print(type(list1))
# lost() constractor 
list2 = list(("hello", 22, 44.44, True, 2+9j ));print(list2)

# access list
print(list2[2])
# change list items
list2[1] = 1000
print(list2)
# insert() : add items
list2.insert(2,"world"); print(list2)


