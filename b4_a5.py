def S(n : int, m : int) -> int:
    if n == 0 and m == 0:
        return 1
    if m == 0 or n < m:
        return 0
    
    return S(n-1, m-1) + m*S(n-1, m)

if __name__ == '__main__':
    print(f"S(5,3) = {S(5, 3)}")
