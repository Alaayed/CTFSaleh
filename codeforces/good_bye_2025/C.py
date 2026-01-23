from itertools import accumulate
def solve():
    res = []
    for _ in range(int (input())):
        n = int(input())
        nums = list(map(int , input().split() ))
        # dp[i], optimal assignment for the first i elements
        best_list = list(accumulate(nums[1:], lambda acc, x: acc + abs(x) , initial=nums[0]))
        naughty_list = list(accumulate(nums[::-1], lambda acc, x: acc + x))[::-1]
        naughty_list = list(map(lambda x: -x, naughty_list))
        msum = -float('inf')
        for i in range(n):
            if 0<i<(n-1):
                msum = max(msum , best_list[i-1] + naughty_list[i+1])
            elif i == 0:
                msum = max(msum, naughty_list[i+1])
            else:
                msum = max(msum, best_list[i-1])
        res.append(msum)
    list(map (print, res))
        
solve()