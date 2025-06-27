# Conversion types: w can change types of variable means that when create variable its type is integer, then change in float 

x = 10     # integer number
y = 10.3   # floating number
z = "Hello"  # string

# Two types of conversion
# # 01 Implicit: Done automatically by the compiler when converting smaller data types to larger ones (e.g., int to float).
x = x+y
print(x, " :type of x" ,type(x))
print(y, " :type of y" ,type(y))
print(z, " :type of z" ,type(z))

# # 02 Explicit : Manually done by the programmer using cast operators (e.g., (int)3.14).

age = input("Enter your age:")
age_1 = int(age)
print(type(age_1))
print(age, type(int(age)))


age_2 = int(input("Enter your age:"))
print(age_2, type(age_2))


name = input("Enter your name:")  # input function give str data type by default.
print(name, type(name))
print(name, type(str(name)))