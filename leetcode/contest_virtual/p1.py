import math
from typing import *
class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        ret = []
        while (n != 0):
            log = math.floor(math.log10(n))
            value = n // (10**log)
            ret.append(value * (10**log))
            n -= value * (10**log)
        return ret
sol = Solution()
print(sol.decimalRepresentation(537))
print(sol.decimalRepresentation(106))
print(sol.decimalRepresentation(6))
