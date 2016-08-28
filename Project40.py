def generate_string():
    ret = ''
    for i in range(1,1000000):
        ret += str(i)
    return ret

def test40(champ):
    ret = 1
    for i in range(7):
        ret *= int(champ[10 ** i - 1])
    return ret

champ = generate_string()
result = test40(champ)