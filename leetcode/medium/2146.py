from typing import *
from collections import deque
directions = [(-1,0), (1,0), (0,-1), (0,1)]
def in_bounds(grid, visited, i, j):
        rows = len(grid)
        cols = len(grid[0])
        return 0 <= i < rows and 0 <= j < cols and grid[i][j] != 0 and not visited[i][j]
class Solution:
        def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
                visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
                queue = deque()
                queue.appendleft( (start[0] , start[1]) )
                sel_items = []
                dist = 0
                while queue:
                        (queue, items) = self.bfs_step(grid, queue, pricing, visited, dist)
                        dist +=1 
                        if len(sel_items) + len(items) <= k:
                                sel_items.extend(items)
                        else:
                                rem= k-len(sel_items)
                                items.sort()
                                sel_items.extend(items[:rem])
                        if len(sel_items) == k:
                                break
                sel_items.sort()
                return [ [i,j] for *_, i, j in sel_items]
        def bfs_step ( self,
        grid: List[List[int]],
        queue: Deque[Tuple[int,int]],
        pricing: List[int],
        visited: List[List[bool]],
        dist:int
        ) -> Tuple[ Deque[Tuple[int,int]] , List[ Tuple[int,int,int]]]:
                in_range = []
                nqueue = deque()
                items_found = []
                while queue:
                        (i,j) = queue.pop()
                        if visited[i][j]:
                                continue
                        # add neighbors
                        for dr,dc in directions:
                                nr, nc = i+dr, j+dc
                                if in_bounds(grid, visited, nr, nc):
                                        nqueue.appendleft( (nr,nc) )
                        price = grid[i][j]
                        visited[i][j] = True
                        if price > 1 and pricing[0] <= price <= pricing[1]:
                                items_found.append( (dist, price, i , j) )
                return (nqueue, items_found)

sol = Solution()

grid = [[1,1,1],[0,0,1],[2,3,4]]
pricing = [2,3]
start = [0,0]
k = 3

print(sol.highestRankedKItems(grid, pricing, start, k))
