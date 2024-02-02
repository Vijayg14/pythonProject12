# 30-01-2024\#
a = 5
b = 6
print('a&b:', a&b)
print('a|b:', a|b)
print('a^b:', a^b)
print('~a:', ~a)
print('a<<b:', a<<b)
print('a>>b:', a>>b)
# comparsion
print ("Both operands are integer")
a=5
b=7
print ("a=",a, "b=",b, "a>b is", a>b)
print ("a=",a, "b=",b,"a<b is",a<b)
print ("a=",a, "b=",b,"a==b is",a==b)
print ("a=",a, "b=",b,"a!=b is",a!=b)
# assignment
a = 19
b = 12
a+=b
print("a = ", "type(a) =", type(a))
#logical
x=10
y=18
print("x>12 and y<20", x>12 and y<20)
print("x>12 or y>20", x>12 or y<20)
print(id(x))
# presedence operator
a=28
b=32
c=(a*b)/2-10
print("c is result",c)
# control statements
#if statement
marks = 80
#result = ""
if marks < 30:
   result = "Failed"
elif marks > 75:
   result = "Passed with distinction"
else:
   result = "Passed"
print(result)
# Python3 program to add two numbers
#To define a function that take two integers
# and return the sum of those two numbers
def add(a=20,b=30):
  return a+b
#initializing the variables
num1 = 10
num2 = 5
#function calling and store the result into sum_of_twonumbers
sum_of_twonumbers = add(num1,num2)
#To print the result
print("Sum of two number", sum_of_twonumbers)
# discount
discount = 0
amount = 1200
# Check he amount value
if amount > 1000:
   discount = amount * 10 / 100
print("amount = ", amount - discount)
#using lamda function
add_numbers = lambda x, y: x + y
num1 = 1
num2 = 2
# Call the lambda function to add the two numbers
result = add_numbers(num1, num2)
print("The sum of", num1, "and", num2, "is", result)
# Python code to demonstrate naive
# method to compute gcd ( recursion )
def hcf(a, b):
	if(b == 0):
		return a
	else:
		return hcf(b, a % b)
res2=hcf(20,201)
print("the value is", res2)
#a = 6
#b =4
#print("The gcd of 600 and 480 is : ", end="")
#print(hcf(6, 480))
# nested if
num=9
if num%2==0:
    print("the value is even")
else:
    print("the value is odd")
    if num%3==0:
        print("the value is divisible by 3")
    else :
        print("the value is not divisible by 3")
# match case
def weekday(n):
    match n:
        case 0:
            return "Monday"
        case 1:
            return "Tuesday"
        case 2:
            return "Wednesday"
        case 3:
            return "Thursday"
        case 4:
            return "Friday"
        case 5:
            return "Saturday"
        case 6:
            return "Sunday"
        case _:
            return "Invalid day number"
print(weekday(3))
print(weekday(6))
print(weekday(7))
# class
class my_college:
    def _init_(self,name="mvgr",dept="eee"):
        self.name = name
        self.dept = dept
        print("name is",self.name)
        print("dept is",self.dept)
#new_college = my_college()
#print(new_college)
