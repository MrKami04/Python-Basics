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
# append()
list2.append("chokolate");print(list2)
# extend()
list2.extend(list1);print(list2)
# remove()
list2.remove("chokolate");print(list2)
# pop()
list2.pop(1);print(list2)
# del
del list2[3]; print(list2)
# del list1;print(list1) give error becouse list doesnt exist

# clear()
list1.clear(); print(list1)
# list comprehension
list3 = [12, 3.55, "PYTHON"];[print(x) for x in list3]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

newlist = [x.upper() for x in fruits]
print(newlist)

newlist = ['hello' for x in fruits]
print(newlist)

newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

# sort()
list4 = [ 4,6,8,9,3,2,5,1]
list4.sort(); print(list4);
list4.sort(reverse=True)
print(list4)

# Reverse Order 
list5 = [44, 66, 45, 77, 88,44,44,2]
list5.reverse(); print(list5)

# copy()
mylist1 = list2.copy(); print(mylist1)
mylist2 = list(list5); print(mylist2)
mylist3 = list3[:]; print(mylist3)

# count method
x = list5.count(44); print(x)


# tuple
tup = ("apple", "banana", "cherry", "apple", "cherry")
print(tup);print(len(tup))
# tuple with one item
tup1 = ("Hello",);print(type(tup1)) #this is tuple
tup2 = ("Hello");print(type(tup2)) # this is string

tup3 = tuple((123,345,567,789)); print(tup3)
# access elemnet
print(tup3[3])
# change tuple to list & then list to tuple
y = list(tup3); y[2] = "oyo"
x = tuple(y); print(x)

# add item
y.append(33333); print(y)

# add tuple to tuple
z = ("Hello",)
tup3 += z ; print(tup3)

# remove item but tuple unchangeable so convert into list
thistup = (23, 45, "hollo", True, False)
y1 = list(thistup); y1.remove("hollo");
thistup  = tuple(y1)
print(thistup)

# del thistup; print(thistup) give error tup delete
# unpack tuple
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

# using asterik *: Assign the rest of the values as a list called "red":
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

# join tuple
tuple1 = tup1 + fruits; print(tuple1)

# count()
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5); print(x)


# Sets in python
set1 = {"apple", "banana", "cherry"};print(set1);print(type(set1))

# duplicate remove and unordered and ( [True & 1] and [False & 0] are consider same value) 
set2 = {12, 22, 33, 12,False, 0, 34,34, 45,1, True, 1, 1,1};print(set2);print(len(set2))
# set() constractor
set3 = set(("Hello", 123, 345, 567)); print(set3); print(type(set3))
# add() item
set3.add("python coder"); print(set3)
# update() use to add set from other set
set3.update(set1); print(set3)
# add list into set as
l1 = [12, 23.4, True, "string"]; set1.update(l1); print(set1)
# remove() if item not exist give error
set1.remove("banana"); print(set1)
# discard() if item nit exist then not give error
print(set1); set1.discard("banana"); print(set1)
# pop() but pop() remove in set any random item because pop() take index but set unindexed.
set1.pop(); print(set1)
# clear() : give empty set()
set1.clear(); print(set1)
# del function
# del set1; print(set1)

# 'union() - allow set tuple or '| - (allow only set)'
set4 = set2.union(set3); print(set4)
set4 = set2 | set3; print(set4)
# join set and tuple
tupl1 = tuple((2003, 3004, 5006, 1001))
set5 = set4.union(tupl1); print(set5)
# intersection() or '&- allow only for sets
set6 = {"apple", "banana", "cherry"};set7 = {"google", "microsoft", "apple"}
set8 = set6.intersection(set7); print(set8)
set8 = set6 & set7; print(set8)
# intersection_update()
set6.intersection_update(set7); print(set6)
# difference() or ' - ' 
set6 = {"apple", "banana", "cherry"};set7 = {"google", "microsoft", "apple"}
set9 = set6.difference(set7); print(set9)
set9 = set6 - set7; print(set9)
# difference_update()
set6.difference_update(set7); print(set6)
# symmetric_diference() or ' ^ '
set6 = {"apple", "banana", "cherry"};set7 = {"google", "microsoft", "apple"}
set10 = set6.symmetric_difference(set7); print(set10)
set10 = set6 ^ set7; print(set10)
# symmetric_difference_update()
set6.symmetric_difference_update(set7);print(set6)

# frozenset
x = frozenset({"apple", "banana", "cherry"})
print(x);print(type(x))


# dictionary
dict1 = {"brand": "Ford","model": "Mustang","year": 1964}
print(dict1);print(type(dict1));print(dict1["brand"]); print(len(dict1))
# duplicate: override duplicate on already exist item
dict2 = {"brand": "Ford","model": "Mustang","year": 1964,"year":2020}
print(dict2); print(type(dict2))
# dict() constractor
dict3 = dict(name = "John", age = 36, country = "Norway"); print(dict3)
# access item
x = dict3["name"];print(x)
x122 = dict3.get("name");print(x122)
# keys()
y112 = dict3.keys(); print(y112)
# values()
y122 = dict3.values(); print(y122)
# item(s)
y211 = dict3.items(); print(y211)
# change items
dict3["name"] = "python"; print(dict3)
# update()
dict3.update({"model":121}); print(dict3)
# pop() remove with spcefic key name
dict3.pop("model"); print(dict3)
# popitem() remove random item
dict3.popitem(); print(dict3)
del dict3["name"]; print(dict3)
# clear() - give empty dict
dict3.clear(); print(dict3)
# copy()
dict2 = {"brand": "Ford","model": "Mustang","year": 2001,"year":2000}
mydict = dict2.copy(); print(mydict)
# dict()
mydict1 = dict(dict2); print(mydict1)
# nested dict
myfamily = {"child1" : {"name" : "Emil","year" : 2004},
  "child2" : {"name" : "Tobias","year" : 2007},
  "child3" : {"name" : "Linus","year" : 2011}}
print(myfamily)
# Access Items in Nested Dictionaries
print(myfamily["child2"]["name"])


