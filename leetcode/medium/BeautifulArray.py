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
        while even:
            inc += 1
            popped = even.pop(0)
            print(f'popped: {popped}')
            # Don't care about odd after
            while odd and odd[0] < popped:
                odd.pop(0)
            temp = even
            even = odd
            odd = temp
        n = len (nums)
        if (n-inc) % 2 != 0:
            inc += 1
        return inc
        def optimizedVersion(self, nums: List[int] ):
            prev = -1
            inc = 0
            # always maintain the condition prev = nums[k-1] where k is odd
            # Trivially true in the inital case

            for n in nums:
                if n == prev: # keep deleting while condition nums[k] == nums[k-1] where k is odd
                    inc+=1
                else:
                    if prev == -1:
                        prev = n
                    else:
                    # condition is false, SKIP current n
                    # to maintain prev = nums[k] where k is odd
                    # Since n is at even index
                        prev = -1
            return inc + (len(nums) - inc)%2

sol = Solution()

nums =[1,1,2,3,5]
print(sol.minDeletion(nums))
nums= [1,1,2,2,3,3]
print(sol.minDeletion(nums))
nums = [1,6,0,9,8,8,4,1,7,1,1,8,9,1,9,1,2,3,7,6,6,8,7,5,9,7,3,0,4,9,1,8,3,3,2,4,2,6,2,8,9,2,8,4,0,1,0,9,9,5]
sol.minDeletion(nums)
