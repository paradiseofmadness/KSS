import random
import numpy

# einseitiger Fehler kein false negativ
def testMatrixMultMC(a:list[list], b:list[list], c:list[list]) -> bool:
    # Laufzeit O(n) + O(n^2) + O(n^2) + O(n^2) + O(n) = O(n^2)

    n = len(a)

    x = [[random.choice([-1, 1])] for _ in range(n)] # O(n)

    arra = numpy.array(a) # n x n
    arrb = numpy.array(b) # n x n
    arrc = numpy.array(c) # n x n
    arrx = numpy.array(x) # n x 1

    # (n x n)*(n x 1) -> (n x 1) => O(n^2) nach Aufgabe 1
    bx = numpy.matmul(arrb, arrx)

    # (n x n)*(n x 1) -> (n x 1) => O(n^2) nach Aufgabe 1
    abx = numpy.matmul(arra, bx)

    # (n x n)*(n x 1) -> (n x 1) => O(n^2) nach Aufgabe 1
    cx = numpy.matmul(arrc, arrx)

    # Vergleiche n x 1 mit n x 1 Stellenweise => O(n)
    return numpy.array_equal(abx, cx)


if __name__ == "__main__":
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
    print("\n")
