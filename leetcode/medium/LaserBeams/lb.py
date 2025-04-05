class Solution:
	def numberOfBeams(self, bank: List[str]) -> int:
		prev_row = 0
		current_row = 0
		total_beams = 0
		for row in bank:
			current_row =0
			# Find num devices in row
			for char in row:
				# Found Device
				if char == '1':
					current_row += 1
			# Calculate beams from prev row
			if current_row != 0:
				total_beams += current_row * prev_row
				prev_row = current_row
		return total_beams

n,m = map(int, input().split())

