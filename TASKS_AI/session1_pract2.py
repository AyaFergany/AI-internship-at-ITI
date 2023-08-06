for item in [0,1,2,3,4]:
        print(item)
    #
mysum = 0
for i in range(10):
    mysum += i
    print(mysum)
    #
mysum = 0
for i in range(7, 10):
    mysum += i
    print(mysum)
    #
mysum = 0
for i in range(5, 11, 2):
    mysum += i #mysum=mysum+i
    if mysum == 5:
        break
print(mysum)
     


