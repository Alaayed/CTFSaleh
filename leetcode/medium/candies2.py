class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        # 2 cases 
        # limit >= n 
        permutations=0
        for i in range(n): 
            if (n-i) > 0:
                for j in range (n-i):
            else:
                permutations+=1 
            for k in range (n-i-j):
        # limit < n
        return 1