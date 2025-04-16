import ast
from typing import List, Tuple


def check_condition(pair: Tuple[int,int,int], k: int, limit: int) -> int:
	if pair[0] == k and pair[1] <= limit:
		return pair[1]
	else:
		return -1


class Solution:
	def maxProduct(self, nums: List[int], k: int, limit: int) -> int:
		max_prod = -1
		# dp[i] all alternating sum product pairs starting from i
		# dp[i] = (dp[i+1]*-1 + nums[i] , dp[i+1]*nums[i])
		dp = [[] for _ in range(len(nums))]

		# Base Case
		dp[-1] = [(nums[-1], nums[-1], -1)]
		max_prod = max(max_prod, check_condition(dp[-1][0], k, limit))
		# Write out the definitions
		for i in range(2, len(nums) + 1):
			val = nums[-i]
			# definitions reliant of prev entry

			for sum, product, prev_product in dp[-i + 1]:
				included = (val - sum, val * product, product)
				# skip i+1'th element
				alt_sum = sum - nums[-i + 1]
				# 2 - 3 + 4 -> -3 + 4
				not_included = (val + alt_sum, val * prev_product, prev_product)
				# skip if product > limit
				if included[1] <= limit:
					dp[-i].append(included)
				if not_included[1] <= limit:
					dp[-i].append( not_included )
				# Check for max prod
				max_prod = max(max_prod, check_condition(included, k, limit))
				max_prod = max(max_prod, check_condition(not_included, k, limit))

			# Add base
			base = (val, val, -1)
			dp[-i].append(base)
			max_prod = max(max_prod, check_condition(base, k, limit))
		return int(max_prod)


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
