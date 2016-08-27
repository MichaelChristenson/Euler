def diag(n):
    corner = []
    a = (2 * n - 1) ** 2
    b = (2 * n - 3) ** 2
    for i in range(4):
        corner += [int(a - i *((a - b) / 4))]
    return corner

def test28(n):
    a = 1
    for i in range(2,int((n+3)/2)):
        b=0
        for j in diag(i):
            a += j
    return a