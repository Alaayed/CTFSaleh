class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        firstK = s[:k]
        lastSplice= s[k:]
        firstK = firstK[::-1]
        print(firstK , lastSplice)
        return firstK + lastSplice
    
# t= int(input())
# sol = Solution()
# for _ in range(t):
#     s = eval(input())
#     k = eval(input())
    
#     print(sol.reversePrefix(s , k))