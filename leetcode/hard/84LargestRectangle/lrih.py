import bisect as bi
from typing import List


class Solution:
	def largestRectangleArea(self, heights: List[int]) -> int:
		# maintain a list of heights and indices where all h < curHeight
		bounded_heights = []
		# maintain a list of completed heights
		area = []
		for i, height in enumerate(heights):
			# Compute area for h in bh where h > height
			print(f'bounded_heights: {bounded_heights}')
			idx = bi.bisect_right(bounded_heights, (height,-1))
			print(f'idx={idx}')
			if idx <=  len(bounded_heights):
				for j in range(idx, len(bounded_heights)):
					h, index =bounded_heights[j]
					bi.insort(area, h * (i - index) )
					print (f"area : {h * (i - index)}")
			# remove heights
			bounded_heights = bounded_heights[:idx]
			# Add current height to bounded_heights
			bi.insort(bounded_heights, (height, i))

		# We've hit the end, evaluate all remaining heights to area
		for h, index in bounded_heights:
			bi.insort(area, h * (len(heights)-index))
		print(f'area={area}')

		return area.pop()

sol = Solution()
sol.largestRectangleArea([2,1,5,6,2,3])
sol.largestRectangleArea([2,4])
sol.largestRectangleArea([1,1])

