from typing import List
class Solution:
    def candy(self, ratings: List[int]) -> int:
        # get list of sorted indices
        sorted_indices = sorted(range(len(ratings)) , key = lambda i : ratings[i])
        # give each child candy
        inc = len(ratings)
        candies = [ 1  for _ in range(inc)]
        # start with least popular child
        for index in sorted_indices:
            left, right = 0,0
            r = ratings[index]
            # find the max rating of his left and right, assuming he is more popular
            if (index-1) >= 0 and r > ratings[index-1]:
                left = candies[index-1]
            if (index+1) < len(ratings) and r > ratings[index+1]:
                right = candies[index+1]
            min_increase = max(left, right)
            # add the minimum number of cookies he needs to get to clear the condition
            inc += min_increase
            candies[index] = 1 + min_increase
        return inc
