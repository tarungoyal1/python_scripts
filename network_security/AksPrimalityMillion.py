def isPrime(n):
	if n==1:
		return False
	if n==2:
		return True
	if n==3:
		return True
	if n==5:
		return True
	if n==7:
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

n=int(input("Enter n:"))
count=1
num=1
while(count<=n):
    if isPrime(num)==True:
        print(str(count)+" : "+ str(num))
        count+=1
    num+=2

input("Enter any key to exit")
