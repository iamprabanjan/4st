#float
price=45.23
gpa=3.2
distance=5.6
print(f"the price is ${price}")
print(f"your gpa is:{gpa}")
print(f"you ran {distance}km")
#integer
age=19
quantity= 3
num_of_students=50
print(f"ypur age {age} year old")
print(f"ypur are buying {quantity}iteams")
print(f"your class has {num_of_students}students")
#string
name="prabanjan"
food="biriyani"
print(f"your name {name}.S")
print(f"you are prefer to eat{food} in night")
#boolean
is_student=False
if is_student:
    print("you are a student")
else:
    print("you are  not a student")

is_18_above_eligible_for_vote = False
is_18_below_not_eligible_for_vote = False  
if is_18_above_eligible_for_vote:  
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

#define a condition
is_online=False
if is_online:
    print("you are in online")
else:
    print("you are not a offline")
#Type casting =convert one variable data type to another
    str(),int(),float(),bool()

name="prabanjan"
age=19
gpa=3.4
is_student =True
print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))
name=bool(name)
print(name)
#input() function
name=input("What is your name?")
print(f"helo{name}!")
name=input("who old are you?")

print("happy birtday!")
print(f"your age {name} year old")
#To caslculate the arera of rectange
length=float(input("Enter the length"))
width=float(input("Enter the width"))
area=length*width
print(area)
#shoppiong car progeem
iteam=input("what iteam would you like?:")
price=float(input("What is the price of the iteam?:"))
quantity=int(input("How many would you like?:"))
total=price*quantity
print(total)




iteam=input("what iteam would you like?:")
price=float(input("What is the price of the iteam?:"))
quantity=int(input("How many would you like?:"))
total=price*quantity
print(f"you bought {quantity}x{iteam}/s")
print(f"your total is {total}")
