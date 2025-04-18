from typing import List


class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        compFreq = {}
        maxFreq = -1
        # find most frequent complement
        n = len(nums)
        for i in range ( len(nums) // 2):
            comp = nums[i] + nums[n-1-i]
            compFreq[comp] = True
        # find the comp with the max
        minMoves = n+1
        for comp in compFreq:
            minMoves = min(minMoves,self.computeMinMoves(comp, limit, nums))
        return minMoves
    def computeMinMoves(self, comp: float, limit: int, nums: List[int]) -> int:
        moves = 0
        n = len(nums)
        for i in range (len(nums) // 2):
            otherComp = nums[i] + nums[n-1-i]
            diff = abs(otherComp - comp)
            if diff != 0:
                if (limit - nums[i]) >= diff or (limit-nums[n-1-i]) >= diff:
                    moves += 1
                else:
                    moves += 2
        return moves
    
sol = Solution()
nums = [1,2,4,3]
limit = 4
print(sol.minMoves(nums , limit))
nums=[1,2,2,1]
limit =2
print(sol.minMoves(nums , limit))