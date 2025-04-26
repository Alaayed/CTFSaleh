from sys import intern
from typing import List, Set, Tuple
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        lines = self.getLines(points)
        best= 1
        print(f'lines : {lines}')
        for s, i in lines:
            onLine = 0
            for p in points:
                # y-mx = b
                onLine += 1 if (p[1] - s*p[0]) == i else 0
            best = max(onLine , best)
        # check horizontal and vertical lines
        hor = 0
        vert = 0
        for p in points:
            vert += 1 if p[1] == 0 else 0
            hor  += 1 if p[0] == 0 else 0
        best = max(best , hor)
        best = max(best, vert)
        return best
    def getLines(self, points: List[List[int]]) -> Set[Tuple[int,int]]:
        n = len(points)
        origin = False
        print(f'points : {points}')
        lines = set()
        for i in range(n):
            p1 = points[i]
            for j in range(i+1 , n):
                p2 = points[j]
                origin = origin or (p2 == [0,0] or p1 == [0,0])
                deltaX = p1[0] - p2[0]
                deltaY = p1[1] - p2[1]
                print(f'deltax : {deltaX}, deltaY {deltaY}')
                if deltaY == 0:
                    continue
                slope = deltaX / deltaY
                # y - mx = b
                intercept = p1[1] - slope * p1[0]
                lines.add( (slope , intercept) )
        # make lines from all points to origin
        return lines

sol = Solution()
#print(sol.maxPoints(points =[[1,1],[2,2],[3,3]]))
#print(sol.maxPoints(points =[[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))
print(sol.maxPoints(points =[[1,0],[0,0]]))
