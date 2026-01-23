def solve():
    res = []
    for _ in range(int(input())):
        string = input()
        result = 'YES' if string.count('Y') <= 1 else 'NO'
        res.append(result)
    list(map(print , res))
solve()
            
