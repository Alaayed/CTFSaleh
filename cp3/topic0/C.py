def find(x, parent):
    if parent[x] != x:
        parent[x] = find(parent[x], parent)
    return parent[x]

def union(x, y, parent):
    rootX = find(x, parent)
    rootY = find(y, parent)
    if rootX != rootY:
        parent[rootY] = rootX
def is_connected(edges, n):
    parent = list(range(n + 1))
    for u, v in edges:
        union(u, v, parent)
    
    root = find(1, parent)
    for i in range(2, n + 1):
        if find(i, parent) != root:
            return False
    return True

def solve():
    t = int(input())
    for _ in range(t):
        # read and ignore blank lines
        _ = input() 
        n, m = map(int , input().split())
        # construct the adj list
        edges = []
        for _ in range(m):
            u, v, w = map(int , input().split())
            edges.append((u , v , w))
        bestWeight = (1 << 30) - 1
        for i in range(30):
            topbit = 1 << (29 - i)
            candWeight = bestWeight ^ topbit
            filteredEdges = [(u, v) for u, v, w in edges if (w & candWeight) == w]
            if is_connected(filteredEdges, n):
                bestWeight = candWeight
        print(bestWeight)
solve()
