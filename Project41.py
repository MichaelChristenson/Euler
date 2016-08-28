from factor import *

def test41():
    a = [1]
    b = 0
    while len(a) < 9:
        a += [a[-1] + 1]
        c = permute(a)
        for i in c:
            d = reassemble(i)
            if prime(d):
                b = max(d,b)
                print b
    return b

result = test41()