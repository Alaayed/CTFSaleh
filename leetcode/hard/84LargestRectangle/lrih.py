import bisect as bi
from typing import List
debug = False

class Solution:
	def largestRectangleArea(self, heights: List[int]) -> int:
		max_area = 0
		stack = [(heights[0], 0)]
		for i,h in enumerate(heights):
			# When we encounter h < stack[-1][0]

			if debug: print(f'stack: {stack}')
			if debug: print(f'h < stack: {h < stack[-1][0]} h: {h} stack: {stack[-1][0]}' )
			if stack and h < stack[-1][0]:
				# pop the stack until condition fails
				last_pop = 0
				while stack and h < stack[-1][0]:
					# Get height and index
					height, index =stack.pop()
					width = i - index
					last_pop = index
					max_area = max(max_area, height * width )
				# start from the last popped bar.
				stack.append((h, last_pop))
			else:
				stack.append((h,i))
		while stack:
			height, index =stack.pop()
			width = len(heights) - index
			max_area = max(max_area, height * width)
			if debug: print(f'height, index: {height}, {index}. width: {width}, max_area: {max_area}')
		return max_area


sol = Solution()
print(sol.largestRectangleArea([2,1,5,6,2,3]))
print(sol.largestRectangleArea([2,4]))
print(f'sol : {sol.largestRectangleArea([1,1])}')
print(f'sol : {sol.largestRectangleArea([4,2,0,3,2,5])}')
# # #

