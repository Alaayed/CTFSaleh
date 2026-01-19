def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int , input().split())
        # construct the adj list
        adj = [[0 for _ in range(n)] for _ in range(n)]
        u,v,w = map (int , input().split())
        adj[u][v] = w
        adj[v][u] = w
        # 
solve()