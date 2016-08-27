from factor import *

def quad(a,b):
    c=0
    d=2
    while prime(d):
        c+=1
        d = c**2 + a * c + b
    return c

def test27():
    a = 0
    b = 0, 0
    for i in range(-1000, 1000):
        for j in range(-1000, 1000):
            if quad(i,j) > a:
                a=quad(i,j)
                b=i,j
                print a, "\t", b
    return b[0]*b[1]