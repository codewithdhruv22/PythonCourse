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



