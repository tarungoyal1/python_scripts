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
    last = [0,1]
    last.append(qlist[0]*last[-1])
    
    for q in qlist[1:]:
        iv = q*last[-1] + last[-2]
        last.append(iv)
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

def getClosestPrime(odd):
    while isPrime(odd)==False:
        odd  -=1
    return odd



    
username = input("Enter your name:")
p1= int(input("Enter an odd number to generate p1:"))
p1 = getClosestPrime(p1)
print("\np1:"+str(p1))

p2= int(input("\nEnter an odd number to generate p2:"))
p2 = getClosestPrime(p2)
print("\np2:"+str(p2))

n=p1*p2
phi_n = (p1-1)*(p2-1)

print("n="+str(n))

e=int(input("choose your e to give to other party:"))
while e>phi_n or gcd(e,phi_n)!=1:
    e=int(input("properly choose your e to give to other party:"))

print("You chose your e="+str(e)+", you can hand him your n and e")

print("Tell public key  (n and e) of other party:\n")

on = int(input("Please tell n of his public key:"))
oe = int(input("Please tell e of other party:"))

d = FishAlgoInverse(e,phi_n)

print("Now you are ready to communicate:")

opt = int(input("Press 1 to generate message as ciphertext\nPress 2 to decrypt received message\nPress 0 to exit\n"))

while opt!=0:
    if opt==1:
        m = input("Enter your message:")
        mnums = [ord(c) for c in m]
        cipherList = []
        try:
            for mnum in mnums:
                cipherList.append((mnum**oe)%on)
            print(cipherList)
        except:
            pass            
    elif opt==2:
        ptList = []
        while True:
            cr = int(input("Enter each number of message, press 0 to finish:"))
            if cr==0:
                break
            else:
                ptList.append((cr**d)%n)
        try:
            cString = ''.join(chr(cn) for cn in ptList)
            print("Plain text:"+cString)
        except:
            pass   
    opt = int(input("Press 1 to generate message as ciphertext\nPress 2 to decrypt received message\nPress 0 to exit\n"))



input("Enter any key to exit")
