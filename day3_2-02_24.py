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
