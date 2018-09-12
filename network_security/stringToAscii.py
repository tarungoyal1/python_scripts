say = input("Enter:")
mnums = [ord(c) for c in say]
cString = ''.join(chr(cn) for cn in mnums)
print(cString)
