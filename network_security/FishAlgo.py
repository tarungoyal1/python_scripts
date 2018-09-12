def FishAlgoInverse(value,modder):
    if value % 2==0 and modder%2==0:
        print("Numbers should be co-prime, both are even")
        return 0
    if gcd(modder,value)!=1:
        print("Numbers should be co-prime")
        return 0
    
    tv=value
    tm=modder
    qotlist = []
    rem = tm%tv
    qotlist.append(tm//tv)
    while rem !=1:
        tm=tv
        tv=rem
        rem = tm%tv
        qotlist.append(tm//tv)
    qlist = qotlist[::-1]
    print(qlist)
    last = [0,1]
    last.append(qlist[0]*last[-1])
        
    for q in qlist[1:]:
        iv = q*last[-1] + last[-2]
        last.append(iv)
    print(last)
    inv = last[-1]
    if (inv*value)%modder==1:
        return inv
    else:
        return modder-inv
    
def gcd(a,b):
    rem = a%b
    while rem!=0:
        a=b
        b=rem
        rem = a%b
    return b

    
import time
value=int(input( "Enter number preceding mod:"))
modder=int(input("Enter number succeding mod:"))

start = time.time()
inverse = FishAlgoInverse(value,modder)
if inverse!=0:
    print("Mult. Modular Inverse = "+str(inverse))
print(time.time()-start)
input("Press any key to exit")

    
   


    
