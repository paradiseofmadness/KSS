import random

def matVek(a: list[list], b: list[list]) -> list[list]:
    n = len(a)
    res = [[0] for _ in range(n)]
    for i in range(n):
        for ii in range(n):
            res[i][0] = res[i][0] + (a[i][ii] * b[ii][0])
    return res

# einseitiger Fehler kein false negativ
def testMatrixMultMC(a:list[list], b:list[list], c:list[list]) -> bool:
    # Laufzeit/Multiplikationen 3*O(n^2) = O(n^2)

    n = len(a)

    x = [[random.choice([-1, 1])] for _ in range(n)] # n x 1 / Vektor ({-1, 1}^n)

    # Matrix * Vektor => O(n^2)
    bx = matVek(b, x)

    # Matrix * Vektor => O(n^2)
    abx = matVek(a, bx)

    # Matrix * Vektor => O(n^2)
    cx = matVek(c, x)

    return abx == cx


if __name__ == "__main__":
    import numpy
    a = [[random.randint(0, 10) for _ in range(4)] for _ in range(4)]
    b = [[random.randint(0, 10) for _ in range(4)] for _ in range(4)]
    c = numpy.matmul(numpy.array(a), numpy.array(b)).tolist()

    print(f"a = {a}")
    print(f"b = {b}")
    print(f"c = {c}")
    print("")

    print("a*b=c? ist", end=" ")
    for _ in range(10):
        print(testMatrixMultMC(a, b, c), end=", ")
    print("\n")


    a = [[random.randint(0, 10) for _ in range(4)] for _ in range(4)]
    b = [[random.randint(0, 10) for _ in range(4)] for _ in range(4)]
    c = [[random.randint(0, 100) for _ in range(4)] for _ in range(4)]

    ab = numpy.matmul(numpy.array(a), numpy.array(b)).tolist()
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"c = {c}")
    print(f"a*b = {ab}")
    print("")

    print("a*b=c? ist", end=" ")
    for _ in range(10):
        print(testMatrixMultMC(a, b, c), end=", ")
    print("\n")
    
    
    a = [[1, 0], [0, 1]]
    b = [[2, 0], [0, 3]]
    c = [[2, 0], [1, 2]]
    ab = [[2, 0], [0, 3]]
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"c = {c}")
    print(f"a*b = {ab}")
    print("")

    print("a*b=c? ist", end=" ")
    for _ in range(10):
        print(testMatrixMultMC(a, b, c), end=", ")
