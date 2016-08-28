from factor import *

def solutions(num):
    ret = 0
    for i in range(1, num):
        for j in range(i, num):
            k = num - i - j
            if i ** 2 + j ** 2 == k ** 2:
                ret += 1
    return ret

def test39():
    ret = 0
    top = 0
    for i in range(1000):
        sol = solutions(i)
        if sol > top:
            ret = i
            top = sol
    return ret

result = test39()
