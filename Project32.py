from factor import *

def process(sub_list):
    a = 0
    for i in sub_list:
        a += i
        a *= 10
    return a // 10

def math_permute(sequence):
    ret = []
    for i in range(len(sequence) - 2):
        a = process(sequence[:i + 1])
        for j in range(i + 1, len(sequence) - 1):
            b = process(sequence[i + 1:j + 1])
            c = process(sequence[j + 1:])
            if a * b == c:
                ret += [c]
    return ret

def test32():
    ret = []
    for i in permute(num):
        ret += math_permute(i)
    return ret
num = [1,2,3,4,5,6,7,8,9]