class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        avg = 0
        for i in range(k): avg+= nums[i]
        avg /= k
        mavg = avg
        start = 0
        end   = k-1
        while (end < len(nums)-1):
            # remove the start
            avg -= nums[start]/k
            # add the next end piece
            avg += nums[end+1]/k
            # move the window
            start+=1
            end+=1 
            # recheck the mavg
            mavg = max(avg, mavg)
        return mavg
