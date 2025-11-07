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
print("its alright.")
print('he is called pythonista.')

# assign string to variable
name = "pythonista";print(name)
# mulltiline string
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''; print(a)  

# string are array
b = "pythonista"
print(b[0]); print(b[2]); print(b[5])
# looping through a string
for char in b:
    print(char)
    
print(len(b))  # length of string
# check string
txt = "The best things in life are free!"
print("free" in txt)
if "free" in txt:
  print("Yes, 'free' is present.")
  print("expensive" not in txt)
  
# slicing
b = "pythonista"
print(b[2:7])   # from index 2 to 6
print(b[:5])  # from start to index 4       
print(b[2:])  # from index 2 to end
print(b[-5:-1])  # from index -5 to -2

# upper() string method
a = "hello world"
print(a.upper()); print(a.lower()); print(a.title())
print(a.strip())  # remove whitespace
print(a.replace("h","j"))  # replace h with j
print(a.split(" "))  # split string at space

# string concatenating
a = "hello"
b = "world"
c = a + " " + b
print(c)    

# we can combine strings and numbers by using f-strings or the format() method!
age = 25
txt = f"My name is John, and I am {age} years old." 
print(txt)
age = 30
txt = f"My name is John, and I am {age} years old."
print(txt)
txt = "We are the so-called \"Vikings\" from the north.";print(txt)

# boolean
print(10 > 9); print(10 == 9); print(10 < 9)
print(bool("Hello")); print(bool(15))

'''In fact, there are not many values that evaluate to False, except empty values,
such as (), [], {}, "", the number 0, and the value None. And of course the value 
False evaluates to False.'''
print(bool(False)); print(bool(None)); print(bool(0)); print(bool("")); print(bool([]))
print("----------------------------")
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

print("----------------------------")
x = 200
print(isinstance(x, int))
# operators start