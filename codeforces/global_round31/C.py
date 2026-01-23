from math import log2,ceil
def solve():
    t = int(input())
    res =[]
    for _ in range(t):
        n, k = map(int, input().split())
        if k % 2 == 1:
            res.append(' '.join( [str(n)] * k))
        else:
            tight = [0] * k
            loose = []
            maxbits = ceil(log2(10**9))
            for i in range(maxbits+1):
                biti = 1 << (maxbits - i)
                if (biti & n):
                    for j in range(len(tight)-1):
                        tight[j] |= biti
                    for j in range(len(loose)):
                        loose[j] |= biti
                    if tight:
                        loose.append(tight.pop())
                    else:
                        loose[-1] ^= biti
                else:
                    clamped = len(loose) if len(loose) % 2 == 0 else len(loose) -1
                    for j in range(clamped):
                        loose[j] |= biti
            loose.extend(tight)
            res.append( ' '.join(list(map(str, loose))))
                    
                
    list(map(print , res))
solve()