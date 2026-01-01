def solve_slice(substring):
    ops = 0
    for i,j in zip(substring, '2026'):
        if i != j:
            ops+=1
    return ops
def solve():
    t = int(input())
    res = []
    for _ in range(t):
        n = int(input())
        s = input()
        if ('2026' in s or '2025' not in s):
            res.append(0)
            continue
        if ('2025' in s):
            res.append(1)
            continue
        minops = 5
        for i in range(0, len(s)-3):
            minops= min(solve_slice(s[i: i+4]), minops)
        res.append(minops)
    list(map(print, res))
    


solve()