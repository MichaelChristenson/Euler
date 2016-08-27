def coin_range(value, remains):
    itr = remains // value
    return range(0, itr + 1)

def recurse(remains, coins):
    if len(coins) == 1:
        if remains % coins[0] == 0:
            return [[remains // coins[0]]]
        return [[-1]]
    ret = []
    for i in coin_range(coins[0],remains):
        a = recurse(remains - coins[0] * i, coins[1:])
        if [-1] in a:
            continue
        for j in a:
            ret += [[i] + j]
    return ret

def test31(money, coins):
    return recurse(money, coins)

pounds = [200,100,50,20,10,5,2,1]