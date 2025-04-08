from collections import defaultdict, deque
from queue import Queue
from typing import List
from bisect import bisect_left, bisect_right, insort

class Packet:
	def __init__(self, source: int, destination: int, timestamp: int):
		self.source = source
		self.destination = destination
		self.timestamp = timestamp

	def to_list(self):
		return [self.source, self.destination, self.timestamp]

	def __eq__(self, other):
		if not isinstance(other, Packet):
			return False
		return (self.source == other.source and
		        self.destination == other.destination and
		        self.timestamp == other.timestamp)

	def __hash__(self):
		# You can hash a tuple of the attributes
		return hash((self.source, self.destination, self.timestamp))


class Router:
	def __init__(self, memoryLimit: int):
		self.memory = deque()
		self.hashMap = defaultdict(lambda: False)
		self.memoryLimit = memoryLimit
		self.sorted_time = defaultdict(list)

	def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
		# Create the packer
		packet = Packet(source, destination, timestamp)
		# Already in memory
		# print(f"packet {packet}, in memory {packet in self.memory}")
		if self.hashMap[packet]:
			return False
		# Already full
		if len(self.memory) == self.memoryLimit:
			# Oldest packet from memory, remove timestamp, and hash map
			rem = self.memory.popleft()
			idx = bisect_left(self.sorted_time[rem.destination], rem.timestamp)
			if idx <= len(self.sorted_time[rem.destination]):
				self.sorted_time[rem.destination].pop(idx)
			self.hashMap[rem] = False
		# add to memory, timeStamp and hashMap
		self.memory.append(packet)
		self.hashMap[packet] = True
		insort(self.sorted_time[destination] , timestamp)
		return True

	def forwardPacket(self) -> List[int]:
		if self.memory:
			packet = self.memory.popleft()
			self.hashMap[packet] = False
			idx = bisect_left(self.sorted_time[packet.destination], packet.timestamp)
			if idx <= len(self.sorted_time[packet.destination]):
				self.sorted_time[packet.destination].pop(idx)
			return packet.to_list()
		return []

	def getCount(self, destination: int, startTime: int, endTime: int) -> int:
		tList = self.sorted_time[destination]
		return bisect_right(tList, endTime) -bisect_left(tList, startTime)


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)©leetcode


router = Router(3)
router.addPacket(1, 4, 90)
router.addPacket(2, 5, 90)
router.addPacket(1, 4, 90)
