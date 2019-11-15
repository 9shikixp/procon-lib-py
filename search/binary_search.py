import bisect

def binarySearch(A, key):
    left = 0
    # right = n
    right = len(A)
    while left < right:
        mid = (left + right) // 2
        if A[mid] == key:
            # return mid
            return 1
        elif key < A[mid]:
            right = mid
        else:
            left = mid + 1
    # return NOT_FOUND
    return 0


if __name__ == '__main__':
    n = int(input())
    S = list(map(int, input().split()))
    q = int(input())
    T = list(map(int, input().split()))
    ans = 0
    for t in T:
        ans += binarySearch(S, t)
    print(ans)
    
    l = [1, 2, 3, 4, 5, 10, 20, 30, 30, 30, 40]
    print(bisect.bisect_left(l,30))
    # print(bisect.bisect_left(l,29))
    print(bisect.bisect_right(l,30))
    # print(bisect.bisect_right(l,29))
