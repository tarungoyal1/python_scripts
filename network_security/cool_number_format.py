def commanum(num):
    """This is will also accept float values and ignore the decimal"""
    try:
        number = int(num)
    except ValueError as v:
        return ("Could not convert:{}".format(v))
    number = str(number)
    if number.isnumeric() is False:
        raise ValueError("Non-numberic value passed: {}".format(number))
    num = number[::-1]
    cool = [num[i:i + 3][::-1] for i in range(0, len(num), 3)][::-1]
    return ",".join(cool)

def cool_num(number):
    try:
        n = int(number)
    except ValueError as v:
        return "Could not convert the number {}".format(v)

    if n < 1000:
        return str(number)

    full = [1000, 1000000, 1000000000]
    val = ['K', 'M', 'B']

    for f in full[::-1]:
        if n>=f:
            d = n/f
            t = str(d).partition('.')
            if int(list(t[-1])[0]) == 0:
                return "{0}{1}".format(t[0], val[full.index(f)])
            else:
                return "{0:.2f}{1}".format(n/f, val[full.index(f)])