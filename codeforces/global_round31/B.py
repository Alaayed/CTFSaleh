def solve():
    t = int(input())
    res = []
    for _ in range(t):
        n = int(input())
        strings = input().split()
        sol = strings[0]
        for s in strings[1:]:
            flag = False
            # Try both approches char by char
            for i in range(len(s) + len(sol)):
                # s + sol
                preapp = s[i] if i < len(s) else sol[i-len(s)]
                # sol + s
                app    =  sol[i] if i < len(sol) else s[i-len(sol)]
                if app == preapp:
                    continue
                if app < preapp:
                    sol += s
                elif preapp < app:
                    sol = s + sol
                flag = True
                break
            if not flag:
                sol += s
        res.append(sol)
    list(map (print, res))

solve()