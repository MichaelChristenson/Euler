from factor import *

def rotate(parts):
    ret = []
    for i in range(len(parts)):
        ret += [parts[(i + 1) % len(parts)]]
    return ret

def radial(num):
    parts = disassemble(num)
    arc = []
    radial = True
    for j in range(len(parts)):
        degree = reassemble(parts)
        if not prime(degree):
            radial = False
            break
        arc += [degree]
        parts = rotate(parts)
    if radial:
        return arc
    return []

def test35(num):
    circular = []
    for i in range(2,num):
        if prime(i):
            if not i in circular:
                circular += radial(i)
    return circular

result = test35(100)