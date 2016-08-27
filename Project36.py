from factor import *

def test36(num):
    ret = []
    for i in range(num):
        if palindrome(str(i)):
            if palindrome(to_binary(i)):
                ret += [i]
    return ret

result = test36(1000000)