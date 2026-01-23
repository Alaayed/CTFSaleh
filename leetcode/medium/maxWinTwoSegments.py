from typing import *
from collections import Counter
class Solution:
	def maximizeWin(self, prizePositions: List[int], k: int) -> int:
		self.solveOneWindow(prizePositions, k)
		return 0
	def solveOneWindow(self, prizePositions: List[int], k: int) -> int:
		count_pair = Counter(prizePositions).items()

		return 0

sol = Solution()
p=[1,1,2,2,3,3,5]
k = 2
sol.maximizeWin(p, k)