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