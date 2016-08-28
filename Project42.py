def test42(alpha):
    text = open("File42.txt").read().split(',')
    ret = 0
    tri = [1]
    for i in range(1000):
        tri += [tri[-1] + len(tri) + 1]
    for i in text:
        score = 0
        for j in i:
            for k in range(len(alpha)):
                if j == alpha[k]:
                    score += k + 1
                    break
        if score in tri:
            ret += 1
    return ret

alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

results = test42(alpha)