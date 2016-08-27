def factor(num):
    ret = []
    sub = num
    while sub > 1:
        prime = True
        for i in range((ret or [2])[-1], int(sub ** .5) + 1):
            if sub % i == 0:
                sub = int(sub / i)
                ret += [i]
                prime = False
                break
        if prime:
            ret += [sub]
            sub = 1
    return ret

def prime(num):
    if num < 2 or num % 1 != 0:
        return False
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return False
    return True

def disassemble(num):
    a = str(num)
    b = []
    for i in a:
        b += [int(i)]
    return b

def reassemble(parts):
    a = 0
    for i in parts:
        a += i
        a *= 10
    return a // 10

def permute(seed):
    if len(seed) == 1:
        return [[seed[0]]]
    ret = []
    for i in range(len(seed)):
        sub = permute(seed[:i]+seed[i+1:])
        for j in sub:
            ret += [[seed[i]] + j]
    return ret

def unique(seed):
    a = []
    for i in seed:
        if not i in a:
            a += [i]
    return a

def simplify(num,den):
    a = num
    b = den
    reverse = False
    if a > b:
        reverse = True
        a, b = b, a
    num_fac = factor(num)
    den_fac = factor(num)
    for i in range(len(num_fac)):
        for j in range(len(den_fac)):
            if den_fac[j] == num_fac[i]:
                den_fac[j] = 0
                a //= num_fac[i]
                b //= num_fac[i]
    if reverse:
        x = a
        a = b
        b = x
    return a,b

def factorial(num):
    ret = 1
    for i in range(num):
        ret *= i + 1
    return ret

def to_binary(num):
    dum = num
    ret = ''
    while dum > 0:
        ret = str(dum % 2) + ret
        dum //= 2
    return ret

def palindrome(string):
    ret = True
    for i in range(len(string)):
        ret = ret and string[i] == string[-1 - i]
    return ret
