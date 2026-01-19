def even_sol(n):
    if n == 2:
        return "1 2"
    forward_jumps = n // 2 
    backJumps = n//2 + 1
    sol = ""
    cur = n // 2
    jump_count = 0
    while jump_count != n-1:
        sol += f"{cur} "
        if jump_count % 2 == 0:
            cur += forward_jumps
            jump_count += 1
        else:
            cur -= backJumps
            jump_count += 1
    sol += f'{cur} '
    return sol
def solve():
    t = int(input())
    for _ in range(t): 
        n = int(input())
        sol = even_sol( n - (n % 2)).strip()
        sol += f" {n}" if (n % 2) == 1 else ""
        print(sol)
        
         # 1 2 3 4
        # 1 2 3 4 5 
        # 1 2 3 4 5 6 
        # 1 2 3 4 5 6 7
        # 1 2 3 4 5 6 7 8
         

solve()