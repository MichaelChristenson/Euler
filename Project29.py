def process(a,b):
    raw = []
    ret = []
    for i in range(2, a + 1):
        for j in range(2, b + 1):
            raw += [i ** j]
    for i in raw:
        if not i in ret:
            ret += [i]
    return ret