M = 10**9+7
def pow(x, n):
    if n == 0:
        return 1
    res = pow(x * x % M, n//2)
    if n % 2 == 1:
        res = res * x % M
    return res

if __name__ == "__main__":
    m, n = map(int, input().split())
    ans = pow(m, n)
    print(ans)