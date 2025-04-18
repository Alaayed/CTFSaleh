from typing import List , Tuple 
class Solution:
    def countAndSay(self, n: int) -> str:
        prev = '1'
        for i in range(n-1):
            prev = self.freqToString(self.freq(prev))
        return prev
    def freq(self, s: str) -> List[Tuple[chr, int]]: 
        prev = s[0]
        inc = 0
        frequency = []
        for c in s:
            if c == prev:
                inc += 1
            else:
                frequency.append( (prev , inc))
                prev = c
                inc = 1
        frequency.append( (s[-1] , inc))
        return frequency
    def freqToString(self, freq: List[Tuple[chr, int]]) -> str:
        res = ''
        for char, num in freq:
            subString = str(num) + char
            res += subString
        return res

sol = Solution()
print(sol.countAndSay(4))