import sys
from typing import Optional


class RollingHash:
    def __init__(self, s: str, mod: Optional[int] = 2147483647) -> None:
        self.h = [0]
        ord_a = ord('a')
        B = 100
        self.mod = mod
        for si in s:
            ti = ord(si) - ord_a + 1
            self.h.append((B * self.h[-1] + ti) % self.mod)

        self.power_100 = [1]
        n = len(s)
        for _ in range(n):
            self.power_100.append((B * self.power_100[-1]) % self.mod)

    def hash_value(self, l: int, r: int) -> int:
        val = self.h[r] - (self.h[l - 1] * self.power_100[r - l + 1] % self.mod)
        if val < 0:
            val += self.mod
        return val


if __name__ == '__main__':
    input = sys.stdin.readline
    N, Q = map(int, input().split())
    S = input().rstrip()
    rh = RollingHash(S)
    for _ in range(Q):
        a, b, c, d = map(int, input().split())
        if rh.hash_value(a, b) == rh.hash_value(c, d):
            print('Yes')
            continue
        print('No')
