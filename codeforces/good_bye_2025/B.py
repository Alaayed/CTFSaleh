def solve():
    res = []
    for _ in range(int(input())):
        s = input()
        uctr = 0
        opctr = 0
        # Handle cases where u cannot be resolved and must me replaced
        # u***u
        if s[0] != 's' and s[-1] != 's':
            s = 's' + s[1:-1] + 's'
            opctr +=2
        elif s[0] != 's':
            s = 's' + s[1:]
            opctr +=1
        elif s[-1] != 's':
            s = s[:-1]+'s'
            opctr += 1
        # For each u block, replace every other u with s
        for e in s:
            if e  == 's': # when we encounter s, change every other u
                opctr += uctr // 2
                uctr = 0
            else: # inc when we encounter u
                uctr += 1
        res.append(opctr)
    list(map(print , res))
solve()