def isPrimitiveRoot(x,n):
    j=n-1
    remList = []
    while j>0:
        remList.append((x**j)%n)
        j-=1
    if remList[0]==1:
        if 1 not in remList[1::]:
            return True
        else:
            return False
    

x = int(input("Enter the number as root:"))
n = int(input("Enter the prime number:"))

if isPrimitiveRoot(x,n):
    print("Yes, "+str(x)+" is primitive root of "+str(n))
else:
    print("No, "+str(x)+" is not a primitive root of "+str(n))
    
