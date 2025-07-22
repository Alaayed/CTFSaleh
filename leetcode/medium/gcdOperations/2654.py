from math import gcd
from typing import List
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        # Initial idea
        ret = n**2
        for i in range(n):
            first = nums[i]
            g = first
            inc = 0
            for j in range(i+1,n):
                second = nums[j]
                g = gcd(first, second)
                inc += 1
                if g == 1:
                    break
                first = g
            if g == 1:
                ret = min(inc, ret)
        print(f'ret: {ret}')
        if ret == n**2:
            ret = -1
        else:
            ret += n-1
        return ret

sol = Solution()
loop = [[2,6,3,4],
[2,10,6,14]]
for l in loop:
    print(sol.minOperations(nums = l))
