from typing import List


class Solution:
	def minimumPairRemoval(self, nums: List[int]) -> int:
		swaps = 0
		while nums != sorted(nums):
			pair_start = 0
			min_sum = float('inf')
			# find the smallest pair
			for i in range(len(nums) - 1):
				if min_sum > nums[i + 1] + nums[i]:
					min_sum = nums[i + 1] + nums[i]
					pair_start = i
			nums[pair_start] = nums[pair_start] + nums.pop(pair_start+1)
			swaps +=1
			print(nums)
		return swaps

s = Solution()
tests = [[5,2,3,1] , [1,2,2]]
for t in tests:
	print(s.minimumPairRemoval(t))
