import sys
def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]
def union(parent, rank, x, y):
    rx = find(parent, x)
    ry = find(parent, y)
    if rx == ry:
        return
    if rank[rx] < rank[ry]:
        parent[rx] = ry
    elif rank[ry] < rank[rx]:
        parent[ry] = rx
    else:
        parent[ry] = rx
        rank[rx] += 1
def is_connected(edges, n ):
    parent  = [i for i in range(n+1)]
    rank    = [1 for _ in range(n+1)]
    # Add all edges
    for u,v in edges:
        union(parent, rank, u, v)
    root = find(parent, 1)
    return all(find(parent, i) == root for i in range(1,n+1))

def solve():
    it = iter(map(int, sys.stdin.read().strip().split()))
    t = next(it)
    for _ in range(t):
        # read and ignore blank lines
        n,m = next(it), next(it)
        # construct the adj list
        edges = []
        for _ in range(m):
            u, v, w = next(it), next(it), next(it) 
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
