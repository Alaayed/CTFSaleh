import random
import numpy as np
class SparseTable:
	def __init__(self, array):
		self.array = array
		self.n = len(array)
		self.table = [ [0 for _ in range(self.n.bit_length())] for _ in range(len(array)) ]
		self.make_table()
	def make_table(self):
		for i in range(len(self.table)): # Base case
			self.table[i][0] = self.array[i]
		# table[i][j]: solution for range query starting from i and extending 2**j
		# Guarantees logarithmic speed for most range queries
		# And constant speed for idempotent operations
		for j in range(1,len(self.table[0])):
			for i in range(self.n - (1 << j)+1): # ensure range fits in 1..n
				srs =i + (1 << j-1) # second range start
				self.table[i][j] = self._operation(self.table[i][j-1] ,
				                       self.table[srs][j-1])
	def _largest_bit_position(self, num): # zero indexed
		return num.bit_length()-1
	def _operation(self, l, r): # operation we use
		return max(l,r)
	def range_query(self,l,r, idempotent=True):
		if idempotent:
			range_length = r-l+1
			bit_position = self._largest_bit_position(range_length)
			new_r = r- (1<< bit_position)+1
			res = self._operation(self.table[l][bit_position]
			                      ,self.table[new_r][bit_position])
			return res
		# imp later
class SparseTester:
	def __init__(self):
		pass
	def mid_test(self, tests):
		array = np.random.randint(0,100,1_000).tolist()
		table = SparseTable(array)
		for _ in range (tests):
			l,r = sorted([random.randint(0,999) for _ in range(2)])
			if max(array[l:r+1]) != table.range_query(l,r,idempotent=True):
				print('ISSUE DETECTED')
		print('NO ISSUES')
tester = SparseTester()
tester.mid_test(1000)