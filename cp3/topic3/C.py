# link: https://codeforces.com/group/xSQ0pfWy2O/contest/668150/problem/C
# Okay, when moving from the jth to jth+1 column,
# We don't have to recompute the max for all the n sliding arrays
# if we have to recompute the value for a sliding array of length k,
# we have to recompute the value for all sliding arrays of length >= k
# make all arrays sparse tables for O(1) max range queries
# Keep a prefix sum for all values that don't need to be recomputed (all values reachable)

class JaggedSparseTable:
	def __init__(self, a):
		self.st = [a[:]]
		n = len(a)
		k = 1
		while (1 << k) <= n:
			prev = self.st[-1]
			step = 1 << (k - 1)
			cur = [
				max(prev[i], prev[i + step])
				for i in range(n - (1 << k) + 1)
			]
			self.st.append(cur)
			k += 1

	def query(self, l, r, idempotent=True):
		if idempotent:
			length = r - l + 1
			k = length.bit_length() - 1
			return max(self.st[k][l], self.st[k][r - (1 << k) + 1])

def solve():
	n,w = map(int,input().split())
	nums = [list(map(int,input().split()))[1:] for _ in range(n)]
	nums = sorted(nums, key=lambda x: len(x))
	tables = [JaggedSparseTable(num) if len(nums) > 2 else None for num in nums]
	res = []
	for j in range(w):
		jth_sum = 0
		# For the jth column
		for i in range(n):
			# contribution of the i'th column
			arr_len = len(nums[i])
			l = max(arr_len-(w-j), 0)
			r = min(j, arr_len-1)
			if tables[i]: ith_contribution = tables[i].query(l,r)
			else: ith_contribution = max(nums[i][l:r+1])
			if ith_contribution < 0:
				if arr_len - (w-j) < 0:
					continue
				if arr_len-1 < j:
					continue
			jth_sum += ith_contribution
		res.append(jth_sum)
	print(*res)
solve()