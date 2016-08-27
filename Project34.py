from factor import *

def check(num):
    parts = disassemble(num)
    whole = 0
    for i in parts:
        whole += factorial(i)
    return whole == num

def test34():
    total = []
    for i in range(3,9999999):
        if check(i):
            total+=[i]
    return total

result = test34()