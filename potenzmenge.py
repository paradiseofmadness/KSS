def potenzmenge(m: list):
    if len(m) == 0:
        return [[]]
    n = m[-1]
    res = potenzmenge(m[:-1])
    for i in range(len(res)):
        res.append(res[i] + [n])
    return res

if __name__ == "__main__":
    for i in range(4):
        print(potenzmenge([x+1 for x in range(i)]))
