def solve():
    t = int(input())
    res = []
    for _ in range(t):
        n = int(input())
        arr = list(map(int , input().split()))
        dp = [0] * n
        # dp[i], time minimized by removing i
        dp[0] = abs(arr[0] - arr[1])
        dp[-1]= abs(arr[-2]-arr[-1])
        for i in range(1, len(arr)-1):
            current_cost = abs(arr[i-1] - arr[i]) + abs(arr[i] - arr[i+1])
            new_cost     = abs(arr[i-1] - arr[i+1])
            dp[i] = current_cost - new_cost
        max_saved = max(dp)
        idx = dp.index(max_saved)
        arr.pop(idx)
        val = 0
        for i in range(len(arr) - 1):
            val += abs(arr[i] - arr[i+1])
        res.append(val)
    list(map(print , res))

solve()