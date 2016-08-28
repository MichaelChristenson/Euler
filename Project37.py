from factor import *

def trunc(num):
    parts = disassemble(num)
    ret = prime(num)
    for i in range(1, len(parts)):
        ret = ret and prime(reassemble(parts[i:]))
        ret = ret and prime(reassemble(parts[:i]))
        if not ret:
            return False
    return True

def gen_primes(num):
    pri = []
    for i in range(2,num):
        if prime(i):
            pri += [i]
    return pri

def test37():
    ret = []
    n=10
    while len(ret) < 11:
        n+=1
        if trunc(n):
            ret += [n]
    return ret

result = test37()