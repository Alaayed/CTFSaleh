from typing import List, Dict, Tuple

class Solution:
	def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
		floydWarshall , vertices=self.floydWarshall(original, changed, cost, source, target)
		ret = 0
		for s , t in zip(source, target):
		# if they don't match
			if (s != t):
				v1,v2 = vertices[s], vertices[t]
				change_cost = floydWarshall[v1][v2]
				# Return if we can't  make the exchange
				if change_cost == float('inf'):
					return -1
				# Otherwise add the cost
				ret += change_cost
		return ret
	
	def floydWarshall(self, original: List[str] , changed: List[str] , cost: List[int], source: str, target : str) -> Tuple[List[List[float]] ,Dict[str, int]]:
		# define chars as ints
		vertices = self.edgesToVertex(source, target, original , changed)
		n = len (vertices)
		dp = [
			[
				float('inf') for _ in range(n)
			]  for _ in range (n) 
		]
		# For each vertex
		for i in range(n):
			dp[i][i] = 0
		# For each edge
		for start , end , c in zip (original , changed, cost):
			s = vertices[start]
			e = vertices[end]
			dp[s][e] = min(dp[s][e], c)
		for k in range(n):
			for i in range(n):
				for j in range(n):
					dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
		print(vertices)
		print(dp)
		return dp , vertices
	# Finds all unique chars and makes them vertices
	def edgesToVertex (self , source: str, target: str, original: List[str], changed: List[str])-> Dict[str , int]:
		joined_list = original + changed
		concat = source + target
		vertices = list(set( concat ).union( set(joined_list) ))
		return { char : idx for idx, char in enumerate(vertices) }   


sol = Solution()

s = "abcd"
t="acbe"
o=["a","b","c","c","e","d"]
ch=["b","c","b","e","b","e"]
c=[2,5,5,1,2,20]

print(f'sol : {sol.minimumCost(s, t, o , ch , c)}')
