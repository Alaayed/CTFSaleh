import bisect as bi
from typing import List


class Solution:
	def largestRectangleArea(self, heights: List[int]) -> int:
		max_area = 0
		stack = [].append((heights[0],0))
		for i,h in enumerate(heights):
			# When we encounter h < stack[-1][0]
			if stack and h < stack[-1][1]:
				# pop the stack until we reach a
				while stack and h < stack[-1][1]:
					height, index =stack.pop()
					max_area = max(max_area, height * index)

			else:
				stack.append((h,i))
		return max_area


sol = Solution()
sol.largestRectangleArea([2,1,5,6,2,3])
sol.largestRectangleArea([2,4])
print(f'sol : {sol.largestRectangleArea([1,1])}')

# # #

