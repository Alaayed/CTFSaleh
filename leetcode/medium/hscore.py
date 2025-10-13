from typing import List
class Solution:
	def hIndex(self, citations: List[int]) -> int:
		citations.reverse()
		h = 1
		hscore= 0
		for c in citations:
			if c >= h:
				hscore = h
			h+=1
		return hscore


sol = Solution()

a=[0,1,3,5,6]
b=[1,2,100]
print(sol.hIndex(a))
print(sol.hIndex(b))
