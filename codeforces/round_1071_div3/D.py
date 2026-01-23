
def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = []
        for i in range(n):
            arr.append((1<<(n-i))-1)
        

        print(' '.join(list(map(str, arr))))
solve()