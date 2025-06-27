# if-else-elif condition: that condition execute on the given satuation is correct or false.

# Example 01
print("---------- Ali go to scholl ---------------")
required_age = 10
ali_age = 5

if ali_age == required_age:
    print("Ali cannot join school!")
elif ali_age < required_age:
    print("Ali can join school!")
elif ali_age<= required_age:
    print("Ali join higher secondry school!")    
else:
    print("Ali can not go to school!")


# Example 02
print("--------- Title : Weather Conditions-----------")

weather = input("Enter your weather condition then i will suggest your activity:  ")
weather = weather.lower() # convert upper letter into lower letter.
print(weather)
if weather == "sunny":
    print("Go for a picnic!")
elif weather == "rainy":
    print("Stay indoor and make a cup of tea and enjoy rainy weather!")
elif weather == 'snowy':
    print("Build a snowman and play with it!")
elif weather == "windy":
    print("Fly a kite and enjoy winding weather!")
else:
    print("Invalid your weather condition!")