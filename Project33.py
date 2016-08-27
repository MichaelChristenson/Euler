from factor import disassemble as dis
from factor import reassemble as rea
from factor import simplify

def check(num, den):
    if num == den:
        return False
    if num % 10 == 0 and den % 10 == 0:
        return False
    num_list = dis(num)
    den_list = dis(den)
    for i in range(len(num_list)):
        for j in range(len(den_list)):
            if num_list[i] == den_list[j]:
                num_neo = rea(num_list[:i] + num_list[i+1:])
                den_neo = rea(den_list[:j] + den_list[j + 1:])
                if den_neo != 0:
                    return float(num)/den == float(num_neo) / den_neo
    return False

def test33():
    a=[]
    for i in range(10,100):
        for j in range(i + 1,100):
            if check(i,j):
                print i,"/",j
                a += [simplify(i,j)[1]]
    return a