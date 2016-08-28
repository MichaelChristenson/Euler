from factor import *

def test38():
    ret = 0
    for i in range(100000):
        digit = []
        n = 1
        while len(digit) < 9:
            digit += disassemble(i*n)
            n += 1
            if digit != unique(digit):
                digit = []
                break
            if 0 in digit:
                digit = []
                break
        if len(digit) == 9:
            ret = max(ret, reassemble(unique(digit)))
    return ret

result = test38()
