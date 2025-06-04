from math import comb
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        # Stars and bars theorem 
        if (n < limit): 
            return comb(n+3-1 , 3-1)

        inc = 0
        for i in range (0, min(limit, n) + 1):
            # Has a lower and upper range
            remaining_stock = n - i
            min_range = max(remaining_stock - limit, 0) 
            max_range = min(limit , remaining_stock)
            number_of_solutions = max(max_range - min_range + 1 , 0)
            inc += number_of_solutions
            print(f'inc: {inc}')
        return inc
    
sol = Solution()
#print(sol.distributeCandies( 5, 2))
#print(sol.distributeCandies(3,3))
#print(sol.distributeCandies(10001,20001))
print(sol.distributeCandies(4,1))