from typing import List


class Solution:
	def minCosts(self, cost: List[int]) -> List[int]:
		ans: List[int] = []
		m: int = cost[0]
		for i in range(len(cost)):
			m = min(m, cost[i])
			ans.append(m)
		return ans
