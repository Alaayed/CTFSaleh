# https://codeforces.com/problemset/problem/577/B

# Almost CERTAINLY some form of DP with one of the states being M
# Ain't no way the bound on m is 1000 for no reason
# Something like dp[cur][j] where the state is;
# Given the first cur elements, is it possible to reach  (some sum) % j == m
# Transition would be dp[cur][j]= max(dp[cur-1][j], dp[cur-1][(j+num[cur])% m], dp[cur][j])
# base cases: dp[i][nums[i] % m] = 1
# We visit each state at most once
# |S| = 10^6 * 10^3 = 10^9
# it's within bounds
# submitted, crashed on test 16 from memory limit failure
# Ah, just realized that was a gigabyte of data the states were storing.
# If you imagine it as a column, I just need two columns.
# The "current" column--the one thats being updated-- and the previous one.
# still 10^9 computations but only 2000 states tracked
# could probably use a python style swap function for fast swaps
def solve():
	n,m = map(int, input().split())
	# make nums 1 indexed, for simplicity and uniformity
	nums = [0] + list(map(int, input().split()))
	dp = [ [False for _ in range(m)] for _ in range(n+1)]
	# Base cases
	for i in range(1, n+1):
		dp[i][nums[i] % m] = True
	for i in range(1, n+1):
		for j in range(0, m):
			dp[i][j] = max(dp[i-1][j] , dp[i-1][(j - nums[i])% m], dp[i][j])
	print('YES' if dp[n][0]  else 'NO')
solve()