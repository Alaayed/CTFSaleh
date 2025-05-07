from math import gcd
from typing import List
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        # Initial idea
        for i in range(n):
            if i+1 == n:
                break
            first = nums[i]
            second = nums[i+1]
            if gcd(first,second) == 1:
                return n
        return -1
