'''
function: A block of code that performs a specific task when called.Helps in code reuse, modularity, 
and clarity.'''
# 01
print("-----____________-----")
def Hello(): #define a function name is 'Hello'
    print("Hello! G")   
Hello()



# 02 
print("-----____________-----")
def text(): #define a function
   text = "Hello! G"
   print(text)  
   print(text)  
   print(text)  
text()



# 03
print("-----____________-----")
def     hello (text):
    
    print(text)
    print(text)
    print(text)
hello("Hello! G")    



# 04
# # defining a function with if else condition
print("-----____________-----")

def calculator(age, text):
    if age == 5:
        print(" Ali can join school.")
    elif age>5:
        print("Ali should go to higher school.")
    else:
        print("Ali is still a baby.")
calculator(2,"ALi")


# 05
# defining a function of future
print("-----____________-----")
def futur_age(age):
    new_age = age + 20
    return new_age
    print(new_age)
futue_predicted_age = futur_age(1)
print(futue_predicted_age)



'''example 01: In the simplest form, a user is asked to type a word, and the program uses .lower() to
convert it entirely to lowercase before displaying it. This ensures that even if the user types in 
capital letters, the program treats everything uniformly.'''
print("-----____________-----")
def letter_case():
    user = input("Enter your lovely word:")
    user = user.lower()   # convert upper letter into lower letter
    print("lowercase word:", user)
letter_case()
    

'''Example 02: In a slightly more advanced example, the program asks for a sentence from the user. 
It then converts the entire sentence to lowercase using .lower() and counts how many times a 
specific lowercase word (like "the") appears in it, ignoring original casing.'''
print("-----____________-----")
def count_word():
    sent = input("Enter your favourite sentence: ")
    sent = sent.lower()
    word_count = "the"
    count = sent.split().count(word_count)
    sum_letter = len(sent.split())
    total_alphate = sum(char.isalpha() for char in sent)

    print(total_alphate)
    print(sum_letter)
    print(f"The word '{word_count}' appears {count} times.")
    
count_word()


# # Example 03 : Write a Python function to find the maximum of three numbers.
print("-----____________-----")
# # method 01
def max_no():
    
    num1 = int(input("Enter the number 01: "))
    num2 = int(input("Enter the number 02: "))
    num3 = int(input("Enter the number 03: "))
    if num1 > num2 and num1>num3:
        print("num1 is Maximum!")
    elif num2 > num3 and num2>num1:
        print("num2 is Maximum")
    else:
        print("num3 is Maximum!")
max_no()    


# # method 02
def max_no():
    num1, num2, num3 = map(int, input("Enter three numbers separated by space: ").split())
    max_numbr = max(num1,num2, num3)
    print("------****------")
    print(f"Maximum number from input three numbers is  {max_numbr}.")
    
max_no()



# # Example 04 : Write a Python function to sum all the numbers in a list.
print("-----____________-----")
def sum_list():
    list1 = [11 , 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19 , 20 ]
    sum_all_list = sum(list1)
    return sum_all_list
print(f"The sum of list is :{sum_list()}")


# # Example 05: Write a Python function to multiply all the numbers in a list.
print("-----____________-----")
print(f"This is simple multiplication: {11*12*13*14*15*16*17*18*19*20}")
def multiply_list():
     list2 = [11 , 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19 , 20 ]
     result = 1
     
     for num in list2:
         result*= num
     return result
 
print(f"This is function  multiplication: {multiply_list()}")



# # Example 6: Write a Python program to reverse a string.
print("-----____________-----")
def reverse_string():
    str1 = input("Enter the cute string here: ")
    # str1 = str1[::-1]
    str1 = ''.join(reversed(str1))
    print(str1)
reverse_string()

'''
# Example 07: Write a Python function to calculate the factorial of a number (a non-negative integer).
# The function accepts the number as an argument.'''
# method 01
print("-----____________-----")
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# Accept the number as input
n = int(input("Enter the number: "))
print(f"Factorial of the number is: {factorial(n)}")
 
# #  method 02
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
# Accept the number as input
n = int(input("Enter the number: "))
print(f"Factorial of the number is: {factorial(n)}")
 
 
 
# #  Example 08: Check if a Number Falls Within a Given Range
# # method 01:
print("-----____________-----")
def chk_no (n, low , high):
    if (low <= n <= high):
        print("number in range.")
        return True
    else:
        print("out off range.")
        return False
        
result = chk_no(11,2,44)
print(result)

# method 02:
def chk_in_range():
    list1 = [11,22,33,44,55,66,77]
    
    if (a in list1):
            print("Yes, in range.")
            return True
    else:
            print("No, not in range.")
            return False
        
a = int(input("Enter the number you wants: "))      
result = chk_in_range()
print("congratulations", result) 


# method 03:
def chk_in_range(a):
    list1 = [11,22,33,44,55,66,77]
    for num in list1:
        if a == num:
            print("Yes, in range.")
            return True
    print("No, not in range.")
    return False

a = int(input("Enter the number you want: "))      
result = chk_in_range(a)
print("Congratulations", result)



# Example 09: Count Uppercase and Lowercase Letters in a String
print("-----____________-----")
def count_upr_lowr_letter():
    str1 = input("Enter the string here: ")
    upper_count = 0
    lower_count = 0
    for char in str1:
        if char.isupper():
            upper_count += 1
            
        elif char.islower():
            lower_count += 1
            
    print("UpperCase letter: ", upper_count)
    print("LowerCase letter: ", lower_count)        
            
count_upr_lowr_letter()        
