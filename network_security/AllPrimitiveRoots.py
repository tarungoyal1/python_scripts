def isPrime(n):
    if n==2:
        return True
    if n==3:
        return True
    if n%2==0:
        return False
    if n%3==0:
        return False   

    i=5
    w=2
    while i*i<=n:
        if n%i==0:
            return False
        i +=w
        w=6-w
    return True

def isPrimitiveRoot(x,n):
    j=n-1
    remList = []
    while j>0:
        remList.append((x**j)%n)
        j-=1
    print(remList[::-1])
    if remList[0]==1:
        if 1 not in remList[1::]:
            return True
        else:
            return False
    

n = int(input("Enter the prime number:"))
if isPrime(n)==False:
    print("Number is not prime")
else:
    i=2
    rootList=[]
    while (i<n):
        if isPrimitiveRoot(i,n):
            rootList.append(i)
        i+=1
    print("\nHere are the roots:\n")
    print(rootList)
input()

    
