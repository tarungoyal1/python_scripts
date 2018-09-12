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


num= int(input("Enter an odd number:"))
generator = 934857438934857438931234567888764345677654465789999876432213568900988765422367899865433467889999887765434568877887444677786655766647457533685854848455432345676543
while isPrime(generator )==False:
    generator  -=1
    
if isPrime(generator )==True:
        print(generator )

input("Enter any key to exit")
