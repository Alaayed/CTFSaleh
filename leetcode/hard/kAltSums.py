import ast
from typing import List, Tuple, Dict

def rec(k: int, limit: int, index: int, current_sum: int, product: int, isOdd: int, nums: List[int], memo: Dict = {} ) -> int:
    key = (index, current_sum, product, isOdd)
    if key in memo:
        return memo[key]
    # base case
    if index == len(nums):
        if current_sum == k and product <= limit and isOdd != 0:
            return product
        else:
            return -1
    # here is the case where we skip
    skip = rec(k=k , limit=limit , index=index+1 ,current_sum=current_sum , product=product , isOdd=isOdd, nums=nums, memo=memo)
    # Starting the sequence
    nskip = -1
    if isOdd == 0:
        # Start sum from index
        current_sum = nums[index]
        product     = nums[index]
        nskip = rec(k=k , limit=limit , index=index+1 ,current_sum=current_sum , product=product , isOdd=2, nums=nums,memo=memo)
    elif isOdd == 1:
        # Continue sum from index
        current_sum = current_sum + nums[index]
        product = product * nums[index]
        product = min(limit+1, product)
        nskip = rec(k=k , limit=limit , index=index+1 ,current_sum=current_sum , product=product , isOdd=2, nums=nums,memo=memo)
    elif isOdd == 2:
        # Continue sum from index
        current_sum = current_sum - nums[index]
        product = product * nums[index]
        product = min(limit+1, product)
        nskip = rec(k=k , limit=limit , index=index+1 ,current_sum=current_sum , product=product , isOdd=1, nums=nums,memo=memo)
    memo[key] = max(skip, nskip)
    return memo[key]

class Solution:
	def maxProduct(self, nums: List[int], k: int, limit: int) -> int:
	   return rec(k=k, limit=limit, index=0 , current_sum=0, product=0, isOdd=0, nums = nums,memo={} );


sol = Solution()
print(sol.maxProduct([0,2,3], -5 , 12))
