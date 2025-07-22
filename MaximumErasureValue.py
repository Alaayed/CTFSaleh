from collections import deque
from typing import *
# Combo of deque and counter
# Probably overkill, but I've been pretty
# class coded since the start of my internship
# If I'd do it again, I'll just use a set
# and running tally, went overkill with this many functions
class FastStack:
	def __init__(self):
		self.stack: Deque[int] = deque()
		self.count: Counter[int] = Counter()
		self.value: int = 0
	def popleft(self):
		item = self.stack.popleft()
		self.count[item] -= 1
		#print(f'Popped: {item} from stack, count: {self.count[item]}')
		if self.count[item] == 0:
			del self.count[item]
		self.value -= item
		return None
	def push(self, item: int) -> None:
		self.stack.append(item)
		self.count[item] += 1
		self.value += item
	def is_in(self, item:int) -> bool:
		return item in self.count
class Solution:
	def maximumUniqueSubarray(self, nums: List[int]) -> int:
		# First, have a stack
		# starting from the start, add to the stack until we encounter
		# a previous element. Pop stack until we get rid of element
		best = -1
		fastStack = FastStack()
		i = 1
		for num in nums:
			#print(f'Itteration: {i}')
			i+=1
			# Check if it is in the stack
			if not fastStack.is_in(num):
				fastStack.push(num)
				best = max(best, fastStack.value)
			else: # Pop until it isn't
				while fastStack.is_in(num):
					fastStack.popleft()
				# add it to the stack
				fastStack.push(num)
		return best


nums = [[4,2,4,5,6],
        [5,2,1,2,5,2,1,2,5]]
for num in nums:
	print(Solution().maximumUniqueSubarray(num))

