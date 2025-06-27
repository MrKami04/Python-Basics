#  input function: that use for user asking something

a = input("Enter the number:")
print(a)


name  = input("Enter your name her:")
greeting = "Hello!"
print(greeting, name)
print("Hello!,", name)

name1 = input("what is your name:")
age  = input("Enter your age here:")
greeting = "Hi!"
print(greeting, name1, "You are still young.")


# start here:
# project 01
# This is a simple project in python on input function.
# Body mass index (BMI),  input weight , height,
# calculate BMI

height = float(input("whta is yoyr height?" ))
weight = float(input("what is your weight? "))
name = input("what is your name: ")

BMI = weight/height**2
BMI
print("My name is ", name,"and my BMI is ", round(BMI,3) )

# end here.





