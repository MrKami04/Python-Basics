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
