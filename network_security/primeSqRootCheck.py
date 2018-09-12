import math
def checkPrime(num): 
 i=2
 while i<=math.sqrt(num):
    if num%i == 0:
        return 0
    i+=1
 return 1

num=int(input("Enter the number:"))
if checkPrime(num):
    print("Prime")
else:
    prime("Not prime")
input("Enter any key to exit:")
