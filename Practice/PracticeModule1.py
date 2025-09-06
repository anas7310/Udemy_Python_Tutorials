#Variables
import math

a=10
b=20

print(a+b)

#Data Types
a=10
b=23.7
c='Hello'
d=False
print(type(a))
print(type(b))
print(type(c))
print(type(d))

#Concatenation
string = "World"
print(c+' '+string)

#Typecasting
int_to_float = float(a)
print(int_to_float) #output: 10.0

float_to_int = int(b)
print(float_to_int) #Output: 23

floor = math.floor(b)
ceil = math.ceil(b)

print(floor) #output: 23
print(ceil)  #output: 24

#Dynamic typing
var = 10
print(var, type(var))

var = 'Hello World'
print(var, type(var))

var = 13.9
print(var, type(var))


#input from user
age = int(input("What is your age?"))
print(f'Your age is {age}')

#simple calculator
#Arithmetic Operators
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(f'Addition: {num1+num2}')
print(f'Subtraction: {num1-num2}')
print(f'Multiplication: {num1*num2}')
print(f'Division: {num1/num2}')
print(f'Modulus: {num1%num2}')
print(f'Floor Division: {num1//num2}')
print(f'Power: {num1**num2}')
print(f'Square of num1: {num1**2}')
print(f'Square root of 25: {math.sqrt(25)}')

#Comparison Operators
if age < 18:
    print("You are not eligible.")
elif 18 < age < 100:
    print("You are eligible")
elif age == 18:
    print("You need to apply for license immediately")
else:
    print("Enter valid age")

a=10
b=10
c='hello'
d='Hello'

print(a==b) #True
print(c==d) #False, Strings comparison is case sensitive
print(a>b)  #False
print(c!=d) #True
print(a>=b) #True
print(a==d) #False

#Logical Operators AND, OR, NOT
x=True
y=False

print("Not X:",not x)
print("Not Y:",not y)
print("OR operator : ",x or y)
print("AND operator: ",x and y)


#Loops
#for loop
for i in range(10):
    print(i, end=" ")