class Solution:
	def productExceptSelf(self, nums: List[int]) -> List[int]:
		t = 1
		prefix = [t := t * i for i in nums]
		t = 1
		# Reverse the nums [2,3,4] to [4, 3, 2]
		suffix = [t := t * i for i in reversed(nums)]
		# Suffix is now [4, 12, 24], reverse to [24, 12, 4] so querying s[2] correctly returns 4
		suffix.reverse()
		res = []
		for i in range(len(nums)):
			prod = 1
			if i != 0:
				prod *= prefix[i-1]
			if i != len(nums)-1:
				prod *= suffix[i+1]
			res.append(prod)
		return res