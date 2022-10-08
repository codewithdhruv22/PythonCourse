#CHAPTER 01 - VARIABLES

# number , character, spelling, decimal , true

name = "Dhruv"
phoneNumber = 89635
isPhoneCharged = True
temperature = 39.5

subscribedToCWD  = False

#Rules
# 1. Spacing Not Allowed
# 2. Starting with numbers not allowed
# 3. Special Characters Not Allowed(Exc. _)
# 4. Name should be related with value
# 5. Variable Name Should be in camelCaseConvention

#Excercise -
# 5 Variables  - Name, PhoneNumber, Address, 10th Percentage , Are you in college ?
# Post In Comment



#02 - DATATYPES



#Varibales

# int  - Integer (1,2,34,3141,-2424)

number = -343

#float - Decimal Number (34.353 , 0.232 , -232.22)

dec_num  = -22.23

#complex  - Complex Number (1+3j , -34j , j)

complex_num = 1+45j

#str  - String/Words/Characters (D , Dhruv, Silver Mall Indore)

address = "Silver mall Indore"
charc = 'D'
word = "Laptop"

#bool - Boolean (True, False)

isRecording = True
isLiked = True
isRaining = False

# Set , Dictionaries , List , Tuple

#Quick Excercise -
# 1. -0.44
# 2. "D H R U V"
# 3. "22.88"
# 4. "True"
# 5. False





#03 - COMMENTS 


# Software - Project - 100-200 - Code File -

# This is an admin name variable
name = "Dhruv"


#COMMENT KIYA

#This is the end of the program IN - LINE COMMENT
age = 23 # This is an age variable

"""MULTI
LINE 
LINE
COMMENT"""

this = 23







#CHAPTER 04 -   Operators





# operand  - variables/data

#Arthmetic Operatrs - Maths Operation
# + - * / % ** //
print(10+2) #Addition
print(45.22 - 12.22) #Subtraction
print(34*55) #Multiplication
print(22/11) #Division
print(22//11) #Floor Division
print(2**9) #Exponential
print(56%34) #Modulus

#Assignment Operator

temp = 21.66
temp += 1 #temp = temp+1
temp -= 10 #temp = temp - 10
temp *= 2 # temp = temp * 2
temp /= 2 #temp = temp / 2
temp %= 3 #temp = temp%3
temp **= 3 # temp = temp**3

# //= , &=, |=, ^= , >>= , <<=

#Comparison Operator
print(10 == 11) # Equal Comp. Operator
print(0 != 1) # Not Equal
print(3>23) # Greater Than
print(3<23) # Less than
print(3>=4) #Greater than or equal
print(4<=7) #Less than or equal to

print("DHRUV " >= "DHRUV")

#Logical Operators

# and = *
print(True and False)
print(False and True)
print(False and False)
print(True and True) # True

# or = +
print(True and False)
print(False and False) #False
print(True and True)
print(False and True)

# not = invert

print(not True) #False
print(not False) #True


#Quick Excercise  -
# 1. print("DHRUV" == 55) # Error, True, False
# 2. print(45.33 - 44)
# 3. print(not(23>22 and 33<22)) # Error, True, False
# 4. a = 33 , b = -28.99 print(a>b)
# 5. a = 33 , b = 44 , c = 0.44 print((a*b-c)**c)










#CHAPTER 05 - F-STRINGS IN PYTHON







name = 34
channel_name = "Programming With Dhruv"

intro = f"Hello, my Name Is {name} and my channel name is {channel_name}"

print(intro)


#Quick Excercise -
"""
Write a program which can write you an application for leave, make variables of name and date
"""




#CHAPTER 04 - Input

name = input("Enter your name : ")
print(f"My name is {name}")


#Quick Excercise -
"""
Write a function to print introduction of a person
Python Intro Maker
"""





# Chapter 07 - Typecasting


num1  = int(input())
num2 = int(input())
add = num1 + num2
print(f"Addition of these two numbers is {add}")


#Quick Excercise  -
"""
Make A Calculator which can add two decimal number and then multiply it with an integer.

num1 -- Float
num2 -- Float
num3 -- Integer

num1+num2
res*num3
finalRes -- Integer
"""




#Chapter 08 - Lists



#Saman
# Multiple item(data - str,int,float) ek single variable me store kr sakte hai


car_cmp_list = ["BMW" , "Audi", "Maruti", "Land Rover" , "BMW"]
print(car_cmp_list)
roll_num_list = [301, 304, 206 , 113]
# print(roll_num_list)
rain_forcasting_list = [True, False, True, True, False]
# print(rain_forcasting_list)

mix_list = ["BMW" , 12.99 , True]
# print(mix_list)

cmp_name = roll_num_list[-1]
print(cmp_name)


# sub_list = ["Rohan" , "Ashutosh" , "Sakshi"]
# sub_list_length = len(sub_list)
# print(sub_list_length)


#Quick Excercise -
# Make a program in which all the names of Indians States Will be stored in a list. Then accroding to the user input print the State Name of the respective input index
#
# print a warning => How many items are there in list
# list = [afaa,af,af,a,fa]
# input() = >3 (number)
# print()





#Chapter 9 - List Methods 



car_cmp = ["BMW" , "AUDI" ,"Maruti" , "BMW"  ,"AUDI" , "audi" , "bmw"]
# list.func_name(data)
# print(car_cmp)

#Ek element add kro programmatically
# car_cmp.append("Hyundai")

# print(car_cmp)

#Puri list ko empty
# car_cmp.clear()

# print(car_cmp)

#ek duplicate list bnao
# car_cmp1 = car_cmp.copy()
# print(car_cmp)



stock_avail = [23 , 1212 , 12.33, 55.99, 23.001]
#Ye btao ki car_cmp me
bmw_car_count = stock_avail.count("bmw")
# print(bmw_car_count)

#find the index of maruti
# print(stock_avail.index("audi"))

# print(stock_avail)
#2nd index par tata ki gadi lga do
# stock_avail.insert(2,"tata") #=> ['bmw', 'BMW', 'tata', 'bmw', 'audi', 'maruti', 'audi', 'tata', 'tata', 'audi']
# stock_avail.insert(4,"tata")
# print(stock_avail)


#list me se 4th index wala element remove kr do
# print(stock_avail)
# stock_avail.pop(4)
# print(stock_avail)

#audi ki pehli gadi ko delete kr do
# print(stock_avail)
# stock_avail.remove("audi")
# print(stock_avail)

#list ke order ko reverse
# stock_avail.reverse()
# print(stock_avail)

#stock_avail sort
stock_avail.sort()
print(stock_avail)





#Chapter 10 - Dictionaries


#Normal - Word  = Meaning
#Python - Key = Value

#Creating dictionaries
myDict  = {"key1" : "value1" ,
           "key2" : "value2",
           "key3" : {"key31" : "value31" , "key32" : "value32"},
           12 : "value4",

           23.44 : 34}

print((myDict["key3"])["key32"])

print(len(myDict))
#Quick Excercise -
"""
Create a dictionary in which you will store the information of your family members by using nested Dictionaries.
Then take a input of the family member name and show the information of them.

"""





#Chapter 11 - Set Python




# Set - List - Unique - Unordered - Unchangable/immutable
car_cmp  = ["BMW" , "TATA" , "BMW" ,"KIA"]
car_cmp[0] = "TATA"
print(car_cmp)

car_cmp_set = {"BMW" , "TATA" ,"BMW", "KIA"}
car_cmp_set2 = {"BMW" , "TATA" , "MARUTI" }
print(car_cmp_set.intersection(car_cmp_set2))
car_cmp_set.add("HYUNDAI")
print(car_cmp_set)





#Chapter 12 - Tuple In Python




# List - [] - Duplicates Allowed , Ordered , Changable/mutable
# Set - {} - Duplicates Not Allowed , Unordered , Unchangable/immuabtle
#Tuple - () - Duplicates Allowed , Ordered  , Unchangable/immuabtle


car_cmp = ("TATA" , "TATA" , "ROLLS ROYCE" , "FERRARI", "KIA")
print(len(car_cmp))
print(car_cmp.index("KIA"))
print(car_cmp)




#Chapter 13 - If Else In Python




liked = False

if liked:
    print("Rs.100 Transfer To Viewer")
elif 4==5:
    print("I SHOULD BE RUN1")
elif False:
    print("I SHOULD BE RUN2")
elif False:
    print("I SHOULD BE RUN3")
else:
    print("Rs. 100 Deducted from Viewer Account")






#Chapter 14 - Inline If-Else

marks = 40
#Value if Condition else Value

mar_padegi = True if marks<50 else False

age  = int(input("Enter your age: "))
message = 'you are not eligible to apply' if age<16 else 'have to wait to be turned 18+' if 16<age<=18 else 'you are eligible to apply'
print(message)



#Chapter 15  - For Loop 
# print("Hello World!")
#Looping Statement

car_cmp = ["BMW", "TATA", "KIA", "AUDI"]
for i in range(10):
    print(i)
    for j in range(10):
        print(j)

#Quick Excercise -
# 1
# 2
# 4
# 8
# 2
# 16
# 32
# 64
# 3
# ...

#Max Value  = Comment





