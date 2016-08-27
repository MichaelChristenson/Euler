from factor import disassemble as dis

def check(num, pow):
    parts = dis(num)
    a = 0
    for i in parts:
        a += i ** pow
    return a == num

def test30(limit):
    a = 0
    for i in range(2, limit + 1):
        if check(i,5):
            print i
            a += i
    return a