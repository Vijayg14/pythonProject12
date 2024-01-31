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