def solve():
    t = int(input())
    res = []
    for _ in range(t):
        n = int(input())
        arr = list(map(int , input().split()))
        arr.sort()
        res.append(max (arr[0], arr[1] - arr[0]))
    list(map(print, res))
solve()