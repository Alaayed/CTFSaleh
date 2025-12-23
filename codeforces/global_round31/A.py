def solve():
    t = int(input())
    res = []
    for _ in range(t):
        l,a,b = map(int, input().split())
        dp = [-1 for _ in range(l)]
        current = a 
        best = a
        # Break condition, dp[cur] == ans
        # No better can be done
        while (True):
            best = max(best, current)
            if (best == dp[current]):
                break
            dp[current] = best
            current += b
            current %= l
        res.append(best)
    list(map(print, res))
solve()
