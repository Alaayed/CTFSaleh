import ast
from typing import List, Tuple


def rec(index: int, 
		sum: int,
		prod: int,
		k: int,
		nums: List[int],
		isOdd: bool) -> int:	
	# for now, just implement grabbing all elements	
	
	sign = -1 if isOdd else 1
	ans = rec(index+1,sum + nums[index] * sign, prod * nums[index], k, nums , not isOdd)
	return ans;
class Solution:
	def maxProduct(self, nums: List[int], k: int, limit: int) -> int:
		return 0;		

	
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
