from typing import List
def read_input():
	array: List[List[str]] = []
	index_by: List[str] = []
	with open("lsi.txt") as f:
		for i, line in enumerate(f):
			if i == 6:
				index_by = list(map(str.strip, line.lower().split(",")))
				continue
			# remove d*:
			line = list(map(str.lower, line[4:].split()))
			array.append(line)
	return array , index_by
def stem_list(words: List[str]) -> List[str]:

def lsi():
	docs,  cols = read_input()
	docs: List[List[str]]
	cols: List[str]
	# Now stem cols
	occurences : List[List[int]] = []
	for c in cols:
		c_count = []
		for d in docs:
			c_count.append(d.count(c))
		occurences.append(c_count)
		print(f'{c}: {c_count}')
	print(occurences)
lsi()