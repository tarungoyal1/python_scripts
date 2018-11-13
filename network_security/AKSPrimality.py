def isPrime(n):
    if n<=1:
        return False
    if n==2:
        return True
    if n==3:
        return True
    if n%2==0:
        return False
    if n%3==0:
        return False
    if n%5==0:
        return False
    if n%7==0:
        return False 

    i=5
    w=2
    while i*i<=n:
        if n%i==0:
            return False
        i +=w
        w=6-w
    return True

num= int(input("Enter the number:"))
if isPrime(num)==True:
        print("Number is prime")
else:
    print("Number is not prime")

input("Enter any key to exit")
