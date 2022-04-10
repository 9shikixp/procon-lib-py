from typing import Callable, List, Tuple


class SegmentTree:
    def __init__(self, n_: int, default: float, op: Callable[[int, int], int]) -> None:
        self.default = default
        self.n, self.dat = self.init(n_)
        self.op = op

    def init(self, n_: int) -> Tuple[int, List[int]]:
        n = 1
        while n < n_:
            n *= 2
        dat = [self.default] * (2*n-1)
        return n, dat

    def update(self, k: int, a: int) -> None:
        k += self.n-1
        self.dat[k] = a
        while k > 0:
            k = (k-1) // 2
            self.dat[k] = self.op(self.dat[k * 2 + 1], self.dat[k * 2 + 2])

    def query(self, a: int, b: int, k: int, l: int, r: int) -> int:
        if r <= a or b <= l:
            return self.default
        if a <= l and r <= b:
            return self.dat[k]
        else:
            vl = self.query(a, b, k*2+1, l, (l+r)//2)
            vr = self.query(a, b, k*2+2, (l+r)//2, r)
            return self.op(vl, vr)


if __name__ == "__main__":
    n, q = map(int, input().split())
    seg_tree = SegmentTree(n, 2**31-1, min)
    for i in range(q):
        com, x, y = map(int, input().split())
        if com == 0:
            seg_tree.update(x, y)
        elif com == 1:
            print(seg_tree.query(x, y+1, 0, 0, seg_tree.n))
