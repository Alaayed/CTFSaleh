from typing import List, Set, Tuple
from collections import defaultdict
from fractions import Fraction
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        lines = self.getLines(points)
        best= 1
        for s, i in lines:
            onLine = 0
            for p in points:
                if abs(p[1] - (s * p[0] + i)) < 1e-9:
                    onLine += 1
            best = max(onLine , best)

        # check horizontal and vertical lines
        hor = defaultdict(int)
        vert = defaultdict(int)
        for p in points:
            hor[p[0]] += 1
            vert[p[1]] += 1
        for _,h in hor.items():
            best = max(best , h)
        for _,v in vert.items():
            best = max(best, v)
        return best
    def getLines(self, points: List[List[int]]) -> Set[Tuple[int,int]]:
        n = len(points)
        origin = False
        lines = set()
        for i in range(n):
            p1 = points[i]
            for j in range(i+1 , n):
                p2 = points[j]
                origin = origin or (p2 == [0,0] or p1 == [0,0])
                deltaX = p1[0] - p2[0]
                deltaY = p1[1] - p2[1]
                if deltaX == 0:
                    continue
                slope = deltaY / deltaX
                # y - mx = b
                intercept = Fraction(p1[1]) - slope * Fraction(p1[0])
                lines.add( (slope , intercept) )
        # make lines from all points to origin
        return lines

sol = Solution()
print(sol.maxPoints(points =[[1,1],[2,2],[3,3]]))
print(sol.maxPoints(points =[[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))
print(sol.maxPoints(points =[[1,0],[0,0]]))
print(sol.maxPoints(points =[[2,3],[1,1]]))
points = [[-6,-1],[3,1],[12,3]]
print(Solution().maxPoints(points))
