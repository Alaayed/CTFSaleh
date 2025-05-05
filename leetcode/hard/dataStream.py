from collections import deque
from typing import List
class SummaryRanges:

    def __init__(self):
        self.intervals = []

    def addNum(self, value: int) -> None:
        # New number has 3 cases
        left  = deque()
        right = deque()
        for interval in self.intervals:
            if value >= interval[0] and value <= interval[-1]:
                return
            # 3 On the edge of an interval (extends an interval)
            if value == (interval[0]-1):
                interval.appendleft(value)
                right = interval
            elif value == (interval[-1]+1):
                interval.append(value)
                left = interval
        # join two deques
        if left and right:
            #print(f'left {left} , right {right}')
            left.append(right[-1])
            self.intervals.remove(right)
        elif not left and not right:
            self.intervals.append(deque([value]))

    def getIntervals(self) -> List[List[int]]:
        ret = []
        for d in self.intervals:
            ret.append([d[0],d[-1]])
        ret.sort()
        return ret



# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
