from typing import *
from itertools import combinations_with_replacement
from heapq import heappush, heappop, heapify
class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        # Test if it is possible
        top_range = 1
        for c in cards:
            top_range *= c
        if top_range < 24:
            return False
        # Operator values
        values = {'+': -1, '-': -1, '*': -2, '/' : -2}
        operators = '+-*/'
        parentheses = '(....)'
        all_operators = combinations_with_replacement(operators, 3)
        all_parentheses = permutations = [(x, y) for x in range(4) for y in range(4) if x < y]


        for op in all_operators:
            min_heap = []
            for start, end in all_parentheses:
                for i in range(3):
                    # in parentheses
                    v1 = values[op[i]]
                    if start <= i < end:
                        v1 -= 2
                    # add to heap
                    heappush(min_heap , (v1, i))


