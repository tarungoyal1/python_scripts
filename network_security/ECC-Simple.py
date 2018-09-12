import numpy as np
import random as rand
def getClosePrime(n):
    if checkPrime(n)==True:
        return n
    while checkPrime(n)==False:
        n -= 1
    return n

def checkPrime(n):
    if n%2==0:
        return False
    elif n%3==0:
        return False

    i=5
    w=2
    while i*i<=n:
        if n%i==0:
            return False
        i +=w
        w=6-w
    return True


n = int(input("Enter the maximum limit as prime number:"))
#n = getClosePrime(n)

print("Prime number n is "+str(n))


print("To generate private key, enter any random value for within 1 to "+str(n-1)+":")

d=n+1
while d>n:
    d = int(input("Enter d:"))



p = rand.randint(1,n-1)

q = d * p
print("Q :"+str(q))

print("Your keys are generated.")

while True:
    option = int(input("Enter 1 to encrypt, 2 to decrypt or 0 to exit."))

    if option==1:
        k=n+1
        while k>n:
            k = rand.randint(1,n-1)
            #k = int(input("Enter any random key k for this message within 1 to :"+str(n-1)))
        m = input("Enter message to send:")
        
        mnums = [ord(c) for c in m]
        c1 = k * p
        cipherList = []
        
        print("c1 = "+str(c1))
        print("c2 = \n")  
        try:
            for mn in mnums:
                cipherList.append(mn + k*q)
        except:
            pass
        print(cipherList)
    elif option==2:
        dc1 = int(input("Enter c1 recieved:"))
        dc2 = int(input("Enter c2 recieved:"))
        dm = dc2 - (d * dc1)
        print(chr(dm))
    else :
        break





