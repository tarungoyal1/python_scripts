import numpy as np

def bitwiseXorBinary(a,b):
    y = int(a, 2) ^ int(b, 2)
    y = '{0:0{1}b}'.format(y, len(a))
    return y

def bitwiseANDBinary(a,b):
    y = int(a, 2) & int(b, 2)
    y = '{0:0{1}b}'.format(y, len(a))
    return y


def bitwiseORBinary(a,b):
    y = int(a, 2) | int(b, 2)
    y = '{0:0{1}b}'.format(y, len(a))
    return y


def bitwiseBinaryAddition(a,b):
    a = str(a)
    b= str(b)
    y = int(a, 2) + int(b, 2)
    y = '{0:0{1}b}'.format(y, len(a))
    return y

def binaryNot(n):
	res = ""
	for i in n:
		if i == str(1):
			res = res + str(0)
		else:
			res = res + str(1)
	return res

def leftRotateBinary(n,d):
    a = int(n,2) << d
    rshift = 32 - d
    b = int(n,2) >> rshift
    y = a | b
    y = '{0:0{1}b}'.format(y, len(n))
    return y

def truncate(n, d):
    l = len(n) - 32
    temp = n[l:len(n)]
    # temp = n[0:32]
    return temp

    

def sha(data):
    input = data

    # convert each character in string to ascii value and store it in asciiText list
    asciiText = [ord(c) for c in input]

    # print(asciiText)


    # convert binary value of each ascii code in list
    # if any binary value is less than 8 bits long, pad zeros in front of it else just store the raw binary

    binary = []

    for num in asciiText:
        binValue = np.binary_repr(num)
        if len(binValue) < 8:
            padZeroslen = 8 - len(binValue)
            paddedBinValue = str(0) * padZeroslen + binValue
            binary.append(paddedBinValue)
        else:
            binary.append(binValue)

    # upto here, in binary[] we have padded binary values
    # print(binary)


    # now join the string of binary value and append 1 to the last

    binaryString = ""
    for b in binary:
        binaryString = binaryString + b

    binLen = len(binaryString)

    binaryString = binaryString + str(1)
    # print(binaryString)


    # now pad the binary string with zeros until its length when mod with 512 gives 448

    # 5
    while len(binaryString) % 512 != 448:
        binaryString = binaryString + str(0)

    # now binaryString is 448 bits long
    # print(binaryString)

    # get the length of 8 bits ascii code binary value, see  binLen above
    asciiArrayLenBin = np.binary_repr(binLen)

    # now prepend zeros until asciiArrayLenBin is 64-chars long

    preZerolen = 64 - len(asciiArrayLenBin)

    asciiArrayLenBin = str(0) * preZerolen + asciiArrayLenBin

    # print(len(asciiArrayLenBin))


    # now append this 64 bits long asciiArrayLenBin to your 448 bits long binaryString in step 5

    binaryString = binaryString + asciiArrayLenBin

    # now binaryString is 512 bits long (or number which is divisible by 512 if the input was larger)

    # print(len(binaryString))

    # now break the message of binaryString to array of chunks of 512 (in this is case 1 chunk of 512 will be produced, more would be there if input was larger)


    chunks512 = [binaryString[i:i + 512] for i in range(0, len(binaryString), 512)]

    # print(chunks512)


    wordchunks32 = []

    # now break each chunk of 512 chars long into subarray of chunks of 32 chars long
    for ch512 in chunks512:
        wordchunks32.append([ch512[i:i + 32] for i in range(0, len(ch512), 32)])

    # print(wordchunks32)

    # each sub array will have 16 chunks of 32 bits long chars
    # print(len(wordchunks32[0]))

    numOf512chunks = len(chunks512)

    p = 0

    while p < numOf512chunks:
        for i in range(16, 80):
            wordA = wordchunks32[p][i - 3]
            wordB = wordchunks32[p][i - 8]
            wordC = wordchunks32[p][i - 14]
            wordD = wordchunks32[p][i - 16]

            xorA = bitwiseXorBinary(wordA, wordB)
            xorB = bitwiseXorBinary(xorA, wordC)
            xorC = bitwiseXorBinary(xorB, wordD)

            newWord = leftRotateBinary(xorC, 1)
            # following is not standard
            l = len(newWord) - 32
            appNW = [newWord[l:len(newWord)]]
            wordchunks32[p] = wordchunks32[p] + appNW
        p += 1

    # print(wordchunks32)

    # initialise variables

    h0 = '01100111010001010010001100000001'
    h1 = '11101111110011011010101110001001'
    h2 = '10011000101110101101110011111110'
    h3 = '00010000001100100101010001110110'
    h4 = '11000011110100101110000111110000'

    a = h0
    b = h1
    c = h2
    d = h3
    e = h4

    p = 0

    while p < numOf512chunks:
        for j in range(0, 80):

            if 0 <= j < 20:
                BandC = bitwiseANDBinary(b, c)
                notBandD = bitwiseANDBinary(binaryNot(b), d)
                f = bitwiseORBinary(BandC, notBandD)
                k = '01011010100000100111100110011001'
            elif 20 <= j < 40:
                BxorC = bitwiseXorBinary(b, c)
                f = bitwiseXorBinary(BxorC, d)
                k = '01101110110110011110101110100001'
            elif 40 <= j < 60:
                BandC = bitwiseANDBinary(b, c)
                BandD = bitwiseANDBinary(b, d)
                CandD = bitwiseANDBinary(c, d)
                BandCorBandD = bitwiseORBinary(BandC, BandD)
                finalOr = bitwiseORBinary(BandCorBandD, CandD)
                k = '10001111000110111011110011011100'
            elif 60 <= j < 80:
                BxorC = bitwiseXorBinary(b, c)
                f = bitwiseXorBinary(BxorC, d)
                k = '11001010011000101100000111010110'

            word = wordchunks32[p][j]
            tempA = truncate(bitwiseBinaryAddition(leftRotateBinary(a, 5), f), 32)

            tempB = truncate(bitwiseBinaryAddition(tempA, e), 32)
            tempC = truncate(bitwiseBinaryAddition(tempB, k), 32)

            temp = truncate(bitwiseBinaryAddition(tempC, word), 32)

            # temp = truncate(temp,32)
            e = d
            d = c
            c = truncate(leftRotateBinary(b, 30), 32)
            b = a
            a = temp
            # inner for loop ends
        h0 = truncate(bitwiseBinaryAddition(h0, a), 32)
        h1 = truncate(bitwiseBinaryAddition(h1, b), 32)
        h2 = truncate(bitwiseBinaryAddition(h2, c), 32)
        h3 = truncate(bitwiseBinaryAddition(h3, d), 32)
        h4 = truncate(bitwiseBinaryAddition(h4, e), 32)
        p += 1

        # print("h0=" + h0)
        # print("h1=" + h1)
        # print("h2=" + h2)
        # print("h3=" + h3)
        # print("h4=" + h4)

    hash0 = '%08X' % int(h0, 2)
    hash1 = '%08X' % int(h1, 2)
    hash2 = '%08X' % int(h2, 2)
    hash3 = '%08X' % int(h3, 2)
    hash4 = '%08X' % int(h4, 2)

    hash = hash0 + hash1 + hash2 + hash3 + hash4
    return str.lower(hash)

def getNextFibonnaci(a,b):
    return a+b


# program starts from here
print("Enter nothing to come out of loop")
while True:
    rawinput = input("Enter input:")
    if rawinput=='':
        break
    print(sha(rawinput))




