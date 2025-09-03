from collections import deque
from typing import *
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_pair(s: str, first: str, second: str, value: int) -> Tuple[str, int]:
            stack: Deque = deque()
            score = 0
            for ch in s:
                if stack and stack[-1] == first and ch == second:
                    stack.pop()
                    score += value
                else:
                    stack.append(ch)
            return ''.join(stack), score

        total = 0
        if x > y:
            # Remove 'ab' first
            s, gain = remove_pair(s, 'a', 'b', x)
            total += gain
            s, gain = remove_pair(s, 'b', 'a', y)
            total += gain
        else:
            # Remove 'ba' first
            s, gain = remove_pair(s, 'b', 'a', y)
            total += gain
            s, gain = remove_pair(s, 'a', 'b', x)
            total += gain

        return total