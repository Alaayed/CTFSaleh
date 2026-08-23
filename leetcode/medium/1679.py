from collections import defaultdict 



class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        total = 0
        need = defaultdict(int)
        for n in nums:
            if need[k - n] > 0:
                need[k-n] -=1
                total +=1
            else:
                need[n] +=1

        return total 



