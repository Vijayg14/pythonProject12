# class
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
    print("Hello my name is " + self.name)
p1 = Person("ram" , 500)
p1.myfunc()
# string in class
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def __str__(self):
    return f"{self.name}({self.age})"
p1 = Person("Jo", 36)
print(p1)
# inheritance
# Inheritance allows us to define a class that inherits
# all the methods and properties from another class
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
#Use the Person class to create an object, and then execute the printname method:
x = Person("John", "Doe")
x.printname()
#terator
mytuple = ("apple", "banana", "cherry")
for x in mytuple:
  print(x)
#polymorphism
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(len(thisdict))
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
  def move(self):
    print("Fly!")
car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")
for x in (car1, boat1, plane1):
  x.move()
#modules
  import basics13
a = basics13.person1['age']
print(a)
# dates
import datetime
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))
import datetime
x = datetime.datetime(2020, 5, 17)
print(x)
import math
x = math.sqrt(64)
print(x)
# class
# Python3 program to
# demonstrate instantiating
# a class
class Dog:

	# A simple class
	# attribute
	attr1 = "mammal"
	attr2 = "dog"

	# A sample method
	def fun(self):
		print("I'm a", self.attr1)
		print("I'm a", self.attr2)


# Driver code
# Object instantiation
Rodger = Dog()

# Accessing class attributes
# and method through objects
print(Rodger.attr1)
Rodger.fun()
# self() parameter
class GFG:
	def __init__(self, name, company):
		self.name = name
		self.company = company
	def show(self):
		print("Hello my name is " + self.name+" and I" +
			" work in "+self.company+".")
obj = GFG("John", "GeeksForGeeks")
obj.show()
# _init_ function
# Sample class with init method
class college:
	# init method or constructor
	def __init__(self, name):
		self.name = name
	# Sample Method
	def campus(self):
		print('Hello, my college name is', self.name)
p = college('mvgrce')
p.campus()
# default constructor
class GeekforGeeks:
	# default constructor
	def __init__(self):
		self.geek = "GeekforGeeks"
	# a method for printing data members
	def print_Geek(self):
		print(self.geek)
# creating object of the class
obj = GeekforGeeks()
obj.print_Geek()
# parametrised constructor
class Addition:
	first = 0
	second = 0
	answer = 0

	# parameterized constructor
	def __init__(self, f, s):
		self.first = f
		self.second = s

	def display(self):
		print("First number = " + str(self.first))
		print("Second number = " + str(self.second))
		print("Addition of two numbers = " + str(self.answer))

	def calculate(self):
		self.answer = self.first + self.second


# creating object of the class
# this will invoke parameterized constructor
obj1 = Addition(1000, 2000)

# creating second object of same class
obj2 = Addition(10, 20)

# perform Addition on obj1
obj1.calculate()

# perform Addition on obj2
obj2.calculate()

# display result of obj1
obj1.display()
# display result of obj2
obj2.display()
# multiple inheritance
# Python example to show the working of multiple
# inheritance
class Base1(object):
	def __init__(self):
		self.str1 = "Geek1"
		print("Base1")
class Base2(object):
	def __init__(self):
		self.str2 = "Geek2"
		print("Base2")
class Derived(Base1, Base2):
	def __init__(self):

		# Calling constructors of Base1
		# and Base2 classes
		Base1.__init__(self)
		Base2.__init__(self)
		print("Derived")
	def printStrs(self):
		print(self.str1, self.str2)
ob = Derived()
ob.printStrs()
# multilevel inheritance
# Python program to demonstrate
# multilevel inheritance
# Base class
class Grandfather:

	def __init__(self, grandfathername):
		self.grandfathername = grandfathername

# Intermediate class


class Father(Grandfather):
	def __init__(self, fathername, grandfathername):
		self.fathername = fathername

		# invoking constructor of Grandfather class
		Grandfather.__init__(self, grandfathername)

# Derived class
class Son(Father):
	def __init__(self, sonname, fathername, grandfathername):
		self.sonname = sonname

		# invoking constructor of Father class
		Father.__init__(self, fathername, grandfathername)
	def print_name(self):
		print('Grandfather name :', self.grandfathername)
		print("Father name :", self.fathername)
		print("Son name :", self.sonname)
# Driver code
s1 = Son('Prince', 'Rampal', 'Lal mani')
print(s1.grandfathername)
s1.print_name()
# encapuslation
# Python program to
# demonstrate protected members

# Creating a base class
class Base:
	def __init__(self):

		# Protected member
		self._a = 2

# Creating a derived class
class Derived(Base):
	def __init__(self):

		# Calling constructor of
		# Base class
		Base.__init__(self)
		print("Calling protected member of base class: ",
			self._a)

		# Modify the protected variable:
		self._a = 3
		print("Calling modified protected member outside class: ",
			self._a)


obj1 = Derived()

obj2 = Base()

# Calling protected member
# Can be accessed but should not be done due to convention
print("Accessing protected member of obj1: ", obj1._a)

# Accessing the protected variable outside
print("Accessing protected member of obj2: ", obj2._a)
# method overriding
class Bird:
	def intro(self):
		print("There are many types of birds.")


def flight(self):
	print("Most of the birds can fly but some cannot.")


class sparrow(Bird):
	def flight(self):
		print("Sparrows can fly.")


class ostrich(Bird):
	def flight(self):
		print("Ostriches cannot fly.")


obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()

obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_ost.intro()
obj_ost.flight()
