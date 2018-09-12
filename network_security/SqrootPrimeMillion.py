import math
def checkPrime(num):
 if num%2==0:
    return 0
 if num%3==0:
    return 0
 if num%5==0:
    return 0
 if num%7==0:
    return 0
 if num%9==0:
    return 0
 i=2
 while i<=math.sqrt(num):
    if num%i == 0:
        return 0
    i+=1
 return 1

count=5
num=11
print(str(1)+" : "+ str(2))
print(str(2)+" : "+ str(3))
print(str(3)+" : "+ str(5))
print(str(4)+" : "+ str(7))
while count <=1000000:
    if checkPrime(num):
        print(str(count)+":"+str(num)+" sqr")
        count=count+1
    num+=2
    
input("Enter any key to exit:")
