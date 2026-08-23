class Solution:
	def increasingTriplet(self, nums) -> bool:
		cmin = nums[0]
		isLower = []
		for num in nums:

			isLower.append(cmin < num)
			cmin = min(cmin, num)
		cmax = nums[-1]
		isLarger = []
		for num in reversed(nums):
			isLarger.append(num < cmax)
			cmax = max(cmax, num)
		isLarger.reverse()
		return any( isLower[i] and isLarger[i] for i in range(1, len(nums)-1))
