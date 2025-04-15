import ast
from typing import List
class Solution:
	def maxProduct(self, nums: List[int], k: int, limit: int) -> int:
		# dp[i] all alternating sum product pairs starting from i
		# dp[i] = (dp[i+1]*-1 + nums[i] , dp[i+1]*nums[i])
		dp = [[] for _ in range(len(nums))]
		# Base Case
		dp[-1] = [(nums[-1], nums[-1])]
		# Write out the definitions
		for i in range(2, len(nums) + 1):
			val = nums[-i]
			# definitions reliant of prev entry

			for alt_sum, product in dp[-i + 1]:
				# Assume the subsequenc
				new_pair = (val - alt_sum, val * product)
				dp[-i].append(new_pair)
			# Add base
			base = (val, val)
			dp[-i].append(base)
		# Find all alt_sum == k
		max_prod = -1
		for entry in dp:
			for alt_sum, product in entry:
				if alt_sum == k:
					if product <= limit:
						max_prod = max(max_prod, product)
		print(dp)
		return max_prod


sol = Solution()
import ast

data = []

with open('kAltSums.txt', 'r') as f:
	lines = [line.strip() for line in f]

t = int(lines[0])  # Number of test cases

for i in range(1, t):
	idx = 1 + i * 3
	my_list = ast.literal_eval(lines[idx])
	num1 = int(lines[idx + 1])
	num2 = int(lines[idx + 2])
	data.append((my_list, num1, num2))

for nums, k, limit in data:
	print(sol.maxProduct(nums, k, limit))
