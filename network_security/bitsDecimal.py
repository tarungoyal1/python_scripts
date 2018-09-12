while True:
    bits= int(input("Please enter number of bits:"))
    if bits==0:
        break
    dec =  round(((bits-1)*0.301)+1)
    print(dec)
input("Enter any key to exit")
