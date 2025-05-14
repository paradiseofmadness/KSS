def numdiv(n: int) -> int:
    res = 0
    for i in range(3, n+1):
        if (i//3)*3==i or (i//5)*5==i or (i//7)*7==i or (i//11)*11==i:
            res += 1
    return res

if __name__ == "__main__":
    print(numdiv(100000))