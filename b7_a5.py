import random

def randqs(n: list):
    if len(n) <= 1:
        return n, 0
    v=0
    a = n[:]
    x = a.pop(random.randint(0, len(a)-1))
    res1 = []
    res2 = []
    for i in a:
        # Zählt die Vergleiche
        v += 1
        if i<x:
            res1.append(i)
        else:
            res2.append(i)
    res1, v1 = randqs(res1)
    res2, v2 = randqs(res2)
    # gibt die sortierte Liste und die Anzahl der gebrauchten Vergleiche zurück
    return res1 + [x] + res2, v+v1+v2

x = [56, 64, 58, 61, 75, 86, 17, 62, 8, 50, 87, 99, 67, 10, 74]
print(x)
print("-> ", randqs(x)[0])

"""m: Anzahl der Durchläufe
n: Länge der zu sortierenden Listen"""
def avgLaufzeit(m, n):
    import math
    laufzeit = 0
    for _ in range(m):
        tmp = [random.randint(-1000, 1000) for _ in range(n)]
        res = randqs(tmp)
        laufzeit += res[1]

    avg = laufzeit/m
    erw = n*math.log(n, math.e)
    print("n: ", n, " avg Laufzeit: ", avg, " O(n*ln(n)): ", erw , " Verhältnis: ", avg/erw)


if __name__ == "__main__":
    for i in [50, 75, 100, 200, 250, 500, 1000, 1500, 2000, 2500, 5000]:
        # sortiert 10000 Listen mit i zufälligen Elementen
        avgLaufzeit(10000, i)
