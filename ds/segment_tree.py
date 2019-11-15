INT_MAX = 2**31-1
MAX_N = 10**5

def init(n_):
    n = 1
    while n < n_:
        n *= 2
    dat = [INT_MAX] * (2*n-1)
    return n, dat

def update(k, a):
    k += n-1
    dat[k] = a
    while k > 0:
        k = (k-1) // 2
        dat[k] = min(dat[k * 2 + 1], dat[k * 2 + 2])

def query(a, b, k, l, r):
    if r <= a or b <= l:
        return INT_MAX
    if a <= l and r <= b:
        return dat[k]
    else:
        vl = query(a, b, k*2+1, l, (l+r)//2)
        vr = query(a, b, k*2+2, (l+r)//2, r)
        return min(vl, vr)

if __name__ == "__main__":
    n, q = map(int, input().split())
    n, dat = init(n)
    for i in range(q):
        com, x, y = map(int, input().split())
        if com == 0:
            update(x, y)
        elif com == 1:
            print(query(x, y+1, 0, 0, n))