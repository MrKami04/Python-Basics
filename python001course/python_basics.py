#python
print("Hello, World!")
print("Welcome to python.");print("python is easy language.");print("python is popular language.")
print("python is easy language.", end=" ")
print("python us best language.")
print(344);print(22+44);print(5*6);print(45/9);print(5**3)

# variables in python
a=10; b=20
c=a+b
print("sum:",c)

x,y,z = 5,10,15
print(x); print(y); print(z)

x = y = z = 50
print(x); print(y); print(z)

# unpack of collection
fruits = ["apple","banana","mango"]
x,y,z = fruits
print(x); print(y); print(z)
print(x + y + z)
print(x,y,z)

# number in python
x = 5        # int
y = 3.14     # float
z = 2 + 3j   # complex
print(type(x)); print(type(y)); print(type(z))

# scientific number
a = 1.5e2    # 1.5 * 10^2
b = 2.5e-3   # 2.5 * 10^-3
print(a); print(b)

# random number
import random
print(random.randrange(1,100))  # random integer between 1 and 100

# type casting
x = 5;a = float(x)   # int to float
y = 3.14;b = int(y)     # float to int
z = "10";c = int(z)     # str to int
print(a); print(b); print(c)
# string