import numpy as np
k=1
q=1
flag=0
num = int(input("Enter number:"))

if num%2==0 :
    print("Number is not prime")


while True:
    if (num-1)%(np.power(2,k)) != 0:
        break
    q = (num-1) / (np.power(2,k))
    k+=1

k-=1
print(k)
print(q)
test = (np.power(2,q))%num
if test==1 or test==num-1:
    print("Number is prime")
else :
    for j in range(0,k):
        b1= (np.power(test,2))%num
        if b1==1 :
            print("Number is composite")
            flag=1
            break
        elif b1==num-1:
            flag=1
            print("number may be prime")
            break
        else :
            test = b1
    if flag == 0 :
        print("Number is not prime")
    
input("Enter any key to exit:")
