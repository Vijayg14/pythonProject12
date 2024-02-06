# for loop
num=(23,21,34,53,45)
for i in num:
    i+=i
    print(" the output is i ",i)
#tables
for i in range(1,10):
    for j in range(1,10):
        k=i*j
        print("{:3d}".format(k),end=" ")
    print()
# find the simple interest
# Python3 program to find simple interest
# for given principal amount, time and
# rate of interest.


def simple_interest(p, t, r):
    si = (p * t * r) / 100
    print('The Simple Interest is', si)
    return si
simple_interest(8, 6, 8)
#demo
n=int(input("Enter the number"))
sum=0
for num in range(1,n+1,1):
    sum=sum+num
average=sum/n
print("The average",average)
# find the sum of current and previous number
pv_num=0
for i in range(1,20):
    new_num=pv_num+i
    print("The PV is",new_num)
# while loop
num=0
while num<8:
    num=num+1
print("the value is ",num)