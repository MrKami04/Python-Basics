# Python-Basics
This is python basics to advance coding here.

W3School:
--> Python is a popular programming language.
--> It was created by Guido van Rossum, and released in 1991.
--> Python first program is : ```print("Hello World!.")```


--> creating variable as : ```num1 = 23 ; print(num1)``` or ```myName = str(Python); print(myName)```
--> check type of variable of data: use ```type()``` fuction , ```print(type(num1))``` .
--> variable name are case-sensitive: both are different:  a = 12 & A = 15 

-->There are many techniques to declare a variable name for more readability and clearity as :

--> 01-technique: camel-Case as each word starting letter capital except first letter.
```myName = "Python"; myVariableName = "John"; print(myName,"   ",  myVariableName) ```

--> 02-technique: Pascal-Case as each word start with capital letter.
``` MyVariableName = "John bro"; print(MyVariableName)```

--> 03-technique: snake-case as each word separate with underscore( _ ).
``` my_variable_name = "John-king"; print(my_variable_name) ```

--> multiple value assigne : ```x, y, z = 3, 4, 5; print(x, y, z), a1 = b1 = c1 = "Hello!"; print(a1, b1, c1)```

--> number in python: int, float, complex 
--> can't convert complex number into an other type of number like int & float 
--> but int & float convert type into complex 

--> Random number: import random module

-->> string in python: write charactors or words in single or double qoutes like "xyz", or 'xyz' both are same string .
--> multiline string use three single or double qoutes like ''' ''' or """ """
--> string length find use len() function as print(len(a2))
--> check string present or not use : 'in' and 'not in' fucntion
--> string licing: from start, from end, from mid
-->modify string by upper(), lower(), strip(), replace(), split()
--> concatenate string by plus + operator
--> format string : f-string or {} and format() function
--> escape character: \ "vivik" \

--> boolean in python: only 'True' & 'false'

-->operator in python :
--> Arithmatic operators are: +, -, *, /, %, //, **
-->Assignment operators are: =, +=, -=, *=, /=, %=, //=, **=, &=, |=, ^=, >>=, <<=, :=(walrus operator)
--> comparison operator are: ==, >, <,  >=, <=, !=
--> logical operator: and, or, not
--> Identity operators are : is, is not

--> { == (Equality operator): Checks whether values are equal.
Compares the data stored in the variables. ``` a = [1, 2, 3];b = [1, 2, 3];print(a == b)  # True (same contents)```}
--> { is (Identity operator): Checks whether two variables refer to the same object in memory.
Compares object identity, not value. ``` a = [1, 2, 3];
b = [1, 2, 3];print(a is b)   # False (different memory locations)```}
--> both concept { ```x = y = [10, 20]
print(x == y)   # True (same values)
print(x is y)   # True (same object in memory)```
}

--> membership operaator: in , not in

--> list in python : use to store multiple values in one variable
--> list create by square brakets or list() constractor
--> List items are ordered, changeable, and allow duplicate values.
--> check lenght of list by len() fucntion
--> A list can contain different data types
--> check type of list as type() function
--> access list item by indexing
--> change list items by indexing
--> insert items : insert() function
--> add items by append() function at the end of list
--> extend list: to append element from other list to current list then use extend () function and also element will be add end of list.
--> remove list items : remove(), remove spcefic item
--> remove spcefic index use pop() method and if dont give any index the pop() remove last item.
--> del also remove spcefiy index and also if not give any index then it delete completly list
--> clear(): empties the list but list still remain but no content in 
--> list comprehension offers short syntex for looping through list
--> comprehenesion syntax: newlist = [expression for item in iterable if condition == True]
-->sort() list : by default ascending order if sort decending order argument sort(reverse = True)
--> Reverse Order of the list but not in sorting order 
--> copy list: use copy() method and other way is list() method
--> also make copy by using slice method
--> join list by use these methods: plus(+) operator, extend(), append() 
--> count() list use count() method

-->tuple in python:store miltiple values in single variabel
--> tuple write in round braket ()
--> tuple are ordered and unchengeable and also allow duplicate
--> check length of tuple use len() fucntion
--> create tuple with one item as tup1 = ("hello",) is tuple but tup2 = ("hello") is not tuple
-->tuple() constractor : use to create tuple
--> access tuple alement by indexing values
--> change tuple values : once create tuple the we can't change its values but ifwe want to change then Convert the tuple into a list to be able to change it:
--> add item use append() function
--> remove item but tuple unchangeable now we convert into list fisrt
--> del use delete tuple completely
--> join tuple by plus operator + and multiply tuple by * 
--> count() tuple 


--> Sets in python: to store multiple values in single variable with different data types
--> set create with curly brackets {}.
--> set a collection of which is unordered, unchangeable and unindexed and duplicates are not allowed.
--> [True & 1] and [False & 0 ] are consider same value so remove duplicate in set
--> set() constractor to create set
--> once create set we can't change set but we add & remove items from set
--> we can't access item from set with indexing becuase set are unordered.
-->  add item one use : add() function
--> add item from another set to current set use : update() method
--> also we add tuple , list or dictionary by update() function
--> remove item use remove(), discard(), pop() function but its differet benefits to use.
--> clear() use to empties the set not completely delete.
--> but del use to completely delete set
--> union()  or '|' to use join two set with all items both sets or multiple sets
--> also join set and tuple with union()
--> intersection(): keep only duplicares value ir same values in both sets
--> intersection_update(): use to duplicte but change original set
--> difference() or ' - ':  return only first item present not in second set
--> symmetric_difference(): give only items are not present in both set
--> frozenset(): immuteable means you cannot add or remove elements.
--> frozenset functions: copy(), difference()[-], intersection()[&], isdisjoint(), issubset()[<= / <], issuperset()[>= / >], symmetric_difference()[ ^ ], union()[ | ]


--> dictionary: to store data in key:value pair
--> dictionary are ordered, changeable and not allowed duplicates
--> dict() constractor to create dictionary
--> access dict item by usin key values in square bracket or get() fucntion
--> keys(): give all key values of dict
--> values():  give all values of dict
--> item(): give each item in a dictionary, as tuples in a list.
--> change item
--> update(): dictionary
--> remove items: pop() fucntion, popitem(), del (remov item and also delete completely dictionary)
--> clear(): empties the dictionary
--> copy() method
--> nested dictionary: dictionary in dict
--> Access Items in Nested Dictionaries


