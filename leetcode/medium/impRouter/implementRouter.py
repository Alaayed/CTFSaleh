from queue import Queue
from typing import List


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
class Router:
	def __init__(self, memoryLimit: int):
		self.memory = []
		self.memoryLimit = memoryLimit
	def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
		# Create the packer
		packet = Packet(source, destination, timestamp)
		# Already in memory
		# print(f"packet {packet}, in memory {packet in self.memory}")
		if packet in self.memory:
			return False
		# Already full
		if len(self.memory) == self.memoryLimit:
			self.memory.pop(0)
			self.memory.append(packet)
			return True
		self.memory.append(packet)
		return True

	def forwardPacket(self) -> List[int]:
		if len(self.memory) != 0:
			packet = self.memory.pop(0)
			return packet.to_list()
		return []

	def getCount(self, destination: int, startTime: int, endTime: int) -> int:
		inc = 0
		for packet in self.memory:
			timeStamp = packet.timestamp
			if startTime <= timeStamp <= endTime and packet.destination == destination:
				inc+=1
		return inc

# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)©leetcode


router = Router(3)
router.addPacket(1,4,90)
router.addPacket(2,5,90)
router.addPacket(1,4,90)