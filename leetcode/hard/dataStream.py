from collections import deque
class SummaryRanges:

    def __init__(self):
        self.intervals = []

    def addNum(self, value: int) -> None:
        # New number has 3 cases
        flag = False
        for interval in self.intervals:
            # 1 Not in an interval
            if value < interval[0] or value > interval[-1]:
                continue
            # 2 Fully in an interval
            if value >= interval[0] and value <= interval[-1]:
                flag = True
                break
            # 3 On the edge of an interval (extends an interval)
            if value == (interval[0]-1) or value == (interval[-1]+1):
                if value == (interval[0]-1):
                    interval.extendLeft(value)
                else:
                    interval.extend(value)
                flag = True
                break


    def getIntervals(self) -> List[List[int]]:



# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
