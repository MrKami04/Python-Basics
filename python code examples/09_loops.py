#  while and for loops

# while loops

# x = 0
# while (x<5):
#     print(x)
#     x = x+1

#  for loop

# for x in range(4,11):
#     print(x)



#  Array
# days = ["Mon","Tue","Wed","Thu","Fri","Sat", "Sun"]
# for d in days:
#     print(d)



# days = ["Mon","Tue","Wed","Thu","Fri","Sat", "Sun"]
# for d in days:
#     if (d=="Fri"):break  #break the loop
#     print(d)


# days = ["Mon","Tue","Wed","Thu","Fri","Sat", "Sun"]
# for d in days:
#     if (d=="Fri"):continue  # skip the d
#     print(d)

# Exercise 1: Print first 10 natural numbers using while/for loop.
# # for loop
# for i in range(1,11):
#     print(i)
        
# while loop
# x = 1
# while (x<=10):
#     print(x)
#     x = x + 1         

# Exercise 2: Print the following pattern
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5
# for loop
# row = 5   
# for i in range (1,row + 1 ,1):
    
#     for j in range(1, i+1):
#         print(j, end=' ')
        
#     print("")    

# # while loop

# row = 5
# i = 1
# while i <= row:
#     j = 1
#     while j <=i:
#         print(j, end=" ")
#         j+= 1
        
#     print(" ")
#     i += 1    
    
    
# Exercise 3: Calculate sum of all numbers from 1 to a given number    
# for loop
# method 1:
# num1 = 0
# num2 = int(input("ENTER THE NUMBER: "))

# for i in range ( 1, num2 + 1, 1):
#     num1 += i
# print("\n")
# print("sum is ", num1)
# # method 2
# x = sum(range(1, num2 + 1))
# print("sum is=", x)

# while loop
# n1 = 0
# n2 = int(input("Enter the number: "))
# i = 1
# while i<=n2 :
#     n1 +=i
#     i+=1
    
# print("\n")
# print("sum is ", n1)

# # Exercise 4: Print multiplication table of a given number

# n11 = int(input("Enter the number: "))

# for i in range(1,11,1):
#     print("2 ","x ", i, "=", n11*i )
    
    
     