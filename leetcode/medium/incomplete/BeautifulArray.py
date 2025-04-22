from typing import List
class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        # Iterate through the array front to back
        # Keep track of all i where nums[i] == nums[i+1]
        # Use two queues, even and odd while keeping track of the index
        even = []
        odd = []
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                if i % 2 == 0:
                    even.append(i)
                else:
                    odd.append(i)
        inc = 0
        print(f'even:{even} odd: {odd}')
        while even:
            print(f'HEYEYEYEY')
            inc += 1
            popped = even.pop()
            # Don't care about odd after
            while odd and odd[0] < popped:
                odd.pop()
            temp = even
            even = odd
            odd = temp
        n = len (nums)
        print(f'n : {n}, inc {inc} n-inc: {n-inc} condition {n-inc % 2 != 0}')
        if (n-inc) % 2 != 0:
            inc += 1
        return inc

sol = Solution()

nums =[1,1,2,3,5]
print(sol.minDeletion(nums))
nums= [1,1,2,2,3,3]
print(sol.minDeletion(nums))
