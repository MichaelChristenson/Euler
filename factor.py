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