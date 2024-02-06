# while loop
count =0
while count <10:
    count+=1
print("count is value",count)
# break statement
for i in "python":
    if i =='h':
        break
    print("i is value",i)
# continue
var=10
while var>0:
    var=var-1
    if var==6:
     continue
    print("var is value",var)
#pass
for i in "mvgrce college":
    if i == "ce":
        pass
        print("i value is passes")
    print("i is value",i)
# nested loop
i = 2
while(i < 100):
   j = 2
   while(j <= (i/j)):
      if not(i%j): break
      j = j + 1
   if (j > i/j) :
    print (i, " is prime")
   i = i + 1
# function
def printinfo( name, age = 35 ):
   print ("Name: ", name)
   print ("Age ", age)
   return
printinfo( age=27, name="jagadish" )
printinfo( name="jagadeesh" )
#####
counter = 0
while (counter < 10):
    counter = counter + 1
    print("Python code")  # Executed untile condition is met
else:
    print("Code terminated")
#####
def function( *args_list ):
    ans = []
    for l in args_list:
        ans.append( l.upper() )
    return ans
# Passing args arguments
object = function('Python', 'Functions', 'tutorial')
print( object )
#file read
age = input('Enter your age:')

# convert the string to int
your_age = int(age)
# determine the ticket price
if your_age < 5:
    ticket_price = " not need"
elif your_age < 16:
    ticket_price = 80
else:
    ticket_price = 120
# show the ticket price
print(f"You'll pay for the ticket ",ticket_price)

