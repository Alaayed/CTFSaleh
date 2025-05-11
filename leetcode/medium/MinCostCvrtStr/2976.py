from typing import List

class Solution:
	def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
		mapping = {}
		# map changing each character to it's min cost
		for org , ch , c in zip(original , changed, cost):
			pair= (org, ch)
			mapping[ pair ] = min(mapping.get( pair , float('inf')) , c )
		ret = 0
		for s , t in zip(source, target):
		# if they don't match
			if (s != t):
				change_cost = mapping.get( (s,t) , -1)
# Return if we can't  make the exchange
				if change_cost == -1:
					return -1
# Otherwise add the cost
				ret += change_cost
		return ret


sol = Solution()

s = "abcd"
t="acbe"
o=["a","b","c","c","e","d"]
ch=["b","c","b","e","b","e"]
c=[2,5,5,1,2,20]

print(f'sol : {sol.minimumCost(s, t, o , ch , c)}')
