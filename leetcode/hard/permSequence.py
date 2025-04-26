from typing import List
from math import factorial, ceil
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [i+1 for i in range(n)]
        res = self.rec(nums, k)
        return res
    def rec(self, nums: List[int], k: int) -> str:
        # base case
        if len(nums) == 1:
            return str(nums.pop())
        # find the first digit
        n = len(nums)
        fact = factorial(n-1)
        index = ceil(k/fact) -1
        largest_digit = str(nums.pop(index))
        bounded_k = k % fact
        bounded_k = fact if bounded_k == 0 else bounded_k
        largest_digit += self.rec(nums , bounded_k)
        return largest_digit


sol = Solution()
print(sol.getPermutation(n = 3 , k = 3))

print(sol.getPermutation(n = 4 , k = 9))
print(sol.getPermutation(n = 3 , k = 1))
