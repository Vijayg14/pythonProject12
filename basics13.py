x = 26
y = "jagadish"
print(x)
print(y)
# Casting
print(type(x))
print(type(y))
# numbers
x = 1.10
y = 1.0
z = -35.59
print(type(x))
print(type(y))
print(type(z))
a = 1+2j
b = 2+3j
c = a+b
print(c)
# type conversion
x = 1    # int
y = 2.8  # float
z = 1j   # complex
a = float(x)
b = int(y)
c = complex(x)
print(a)
print(b)
print(c)
# strings
for x in "pythoncode":
  print(x)
String1 = 'Welcome to the pyhton coding'
print("String with the use of Single Quotes: ")
print(String1)
#string slicing
String1 = "mvgr college eee"
print(String1[3:])
#reverse
cd = "mvgr college eee"
#print(cd[::-1])
list2 = list(cd)
list2[2] = 'c'
cd1 = str(list2)
print(cd1)
# string formating
String1 = "{g} {f} {l}".format(g='code', f='For', l='Life')
print("\nPrint String in order of Keywords: ")
print(String1)
# line
ch = "I\ncode\tcode"
print("The string after resolving escape character is : ")
print(ch)
# RegEx
# Python code uses regular expressions to search for the word “portal
#then prints the start and end indices of the matched word within the string
#use RegEx in Python after importing re module.
import re

s = 'GeeksforGeeks: A computer science portal for geeks'
match = re.search(r'portal', s)
print('Start Index:', match.start())
print('End Index:', match.end())
# re find
import re
string = "The quick brown fox jumps over the lazy dog"
pattern = "[a-m]"
result = re.findall(pattern, string)
print(result)
#list
g= ["code", "For", "code"]
print("\nList Items: ")
print(g[0])
print(g[2])
# input for list
#cp = input("enter the list values")
#sp = cp.split()
#print(sp)
# add values
l1 = [2,4,21]
for i in range(4):
  l1.append(i)
print(l1)
#insert
Li = [1, 2, 3, 4]
print("Initial List: ")
print(Li)
Li.insert(3, 12)
Li.insert(0,2)
print("\nList after performing Insert Operation: ")
print(Li)
# Complexities for Adding elements in a Lists(insert() method):
# Time Complexity: O(n)
# Space Complexity: O(1)
# list reversing
mylist = ['code', 2, 32 ,'lit', 'Pyt']
mylist.reverse()
print(mylist)
#pop()
ls = [1, 2, 3, 4, 5]
ls.pop()
print("\nList after popping an element: ")
print(ls)
#coprehension
odd_square = []
for x in range(1, 11):
  if x % 2 == 1:
    odd_square.append(x ** 2)
print(odd_square)
# oops class
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.age)
