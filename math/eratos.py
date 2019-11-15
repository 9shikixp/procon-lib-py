import math
def isprime(x):
    if x == 2:
        return True
    
    if x < 2 or x % 2 == 0:
        return False
    
    i = 3
    while i <= math.sqrt(x):
        if x % i == 0:
            return False
        i = i + 2
    return True

def eratos(n):
    isprime = [True for i in range(n+1)]
    isprime[0] = False
    isprime[1] = False
    for i in range(2, int(math.sqrt(n))+1):
        if isprime[i]:
            j = i + i
        while j <= n:
            isprime[j] = False
            j = j + i
    return isprime        

if __name__ == "__main__":
    # maxn = 10**8
    n = int(input())
    ans = 0
    # isprime = eratos(maxn)
    for i in range(n):
        x = int(input())
        ans += int(isprime(x))
        # ans += int(isprime[x])

    print(ans)
