eob = 0
highest_bits = 1_000_000_000
for i in range(0, highest_bits.bit_length(),2):
    eob |= 1 << i 

def verifier(a,b, layers):
    smallest = min(a,b)
    largest  = max(a,b)
    smask = (1 << layers)-1 & eob
    lmask = (1 << layers)-1 & (eob << 1)
    if smask > lmask:
        smask, lmask = lmask, smask
    return smallest >= smask and largest >= lmask
def solve():
    t = int(input())
    res = []
    for _ in range(t):
        a,b = map(int , input().split())
        abl = a.bit_length()
        bbl = b.bit_length()
        for i in range(22):
            if (not verifier(a,b,i)):
                res.append(i-1)
                break
    list(map(print , res))
solve()