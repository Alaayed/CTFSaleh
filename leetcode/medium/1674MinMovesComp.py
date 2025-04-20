from typing import List


class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        compFreq = {}
        maxFreq = -1
        # find most frequent complement
        n = len(nums)
        minMoves = n+1
        for i in range ( len(nums) // 2):
            comp = nums[i] + nums[n-1-i]
            minMoves = min(minMoves,self.computeMinMoves(comp, limit, nums))
            print(f'comp: {comp}, minMoves: {minMoves}')
        return minMoves
    def computeMinMoves(self, comp: float, limit: int, nums: List[int]) -> int:
        moves = 0
        n = len(nums)
        for i in range (len(nums) // 2):
            otherComp = nums[i] + nums[n-1-i]
            diff = comp - otherComp
            if diff != 0:
                upwardOne = limit-nums[i]
                upwardTwo = limit-nums[n-1-i]
                downWardOne = nums[i]-1
                downWardTwo = nums[n-1-i]-1
                if diff >= 0 and ( upwardOne - diff >= 0 or upwardTwo - diff >= 0):
                    moves += 1
                elif diff < 0 and(downWardOne + diff >= 0 or downWardTwo + diff >= 0):
                    moves += 1
                else:
                    print(f'i: [{i}]')
                    moves += 2
        return moves

sol = Solution()
nums = [1,2,4,3]
limit = 4
print(sol.minMoves(nums , limit))
nums=[1,2,2,1]
limit =2
print(sol.minMoves(nums , limit))
nums=[20744,7642,19090,9992,2457,16848,3458,15721]
limit = 22891
print(sol.minMoves(nums , limit))
