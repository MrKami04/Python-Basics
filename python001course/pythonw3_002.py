# if condition
num1 = 23; num2 = 20
if num1 > num2:
    print("Yes, num1 is greater then num2.")

# variable in condition directly
is_logged_in = True
if is_logged_in:
    print("Welcome! Python.")
    
# Elif condition
if num1 < num2:
    print("num1 is smaller then num2.")
elif num1 > num2:
    print("num1 is greater then num2.")
    
# Multiole elif conditions

day = 4

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thusrday")
elif day == 5:
    print("Friday")

# else condition

age = 19

if age > 18:
    print("You eligible for vote")
elif age >= 13 & age < 13:
    print("You are not eligible.")
else:
    print("You are kid now.")
    
# shorthand if condition

if num1 > num2 : print("num1 is greater then num2.")

# if-else condition
a1 = 4; b1 = 5
print("A") if a1 > b1 else print("B")

# assign values if-else conditon
bigger = a1 if a1 > b1 else b1
print("Bigger is ",bigger)

# multiple condition in one line
a2 = 222; b2 = 333

print("A+") if a2 > b2 else print("=") if a2 == b2 else print("B+")

# logical operators ( and, or, not)

a = 232;  b = 33; c = 53

if (a > b) and (a > c):
    print("a is greater")

elif (b > a) or (b > c):
    print("b is greater")
    
else:
    print("c is greater")
    
# nested if condition
Age = 23;
if Age > 20:
    print("Above 20")
    if Age == 23:
        print("Age is:", Age)
else:
    print("NO age")
    
# pass statement
A = 22; B = 221

if B > A:
    pass