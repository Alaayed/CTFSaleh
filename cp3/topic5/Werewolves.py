# dp[c][sum] where sum represents the freq of the chosen color
# len(dp[c]) = num(k_c) + 1 + num(k_c)-1 == 2*num(k_c)
# e.g. num(k_c) = 300
# -299, -298 ... 0, 1 ... 300
MOD = 998244353


def push_dp(dp, parent: int, child: int, max_count):
	new_dp = dp[parent].copy()  # case: do not take child
	parent_dp = dp[parent]
	child_dp = dp[child]
	lb = -(max_count - 1)
	up = max_count
	for i in range(lb, up + 1):
		cd = child_dp[i]
		if cd == 0: continue  #no contribution
		jlb, jup = max(lb, lb - i), min(up, up - i)
		for j in range(jlb, jup + 1):
			pd = parent_dp[j]
			if pd == 0: continue  #no contribution
			new_dp[i + j] = (new_dp[i + j] + cd * pd) % MOD
	dp[parent] = new_dp


def iterative_dfs(n, colors, current_color, order, parent):
	max_count = sum([1 if c == current_color else 0 for c in colors])  # count total existing colors
	dp = [[0 for _ in range(max_count * 2)] for _ in range(n + 1)]
	limit = [0 for _ in range(n + 1)]
	for i in range(1, n + 1):  # handle base case, subtree is itself
		color_type = 1 if colors[i] == current_color else -1
		if color_type == -1 and max_count != 1:
			dp[i][color_type] = 1
		elif color_type == 1:
			dp[i][color_type] = 1
		limit[i] = 1
	res = 0
	for node in reversed(order):
		res = (res + sum(dp[node][1:max_count + 1])) % MOD
		push_dp(dp, parent[node], node, max_count)
	return res


def get_order_parent(adj, n):
	order = []
	parent = [0 for _ in range(n + 1)]
	parent[1]=-1
	stack=[1]
	while stack:
		node = stack.pop()
		order.append(node)
		for c in adj[node]:
			if c == parent[node]: continue
			parent[c] = node
			stack.append(c)
	return order, parent


def solve():
	n = int(input())
	adj = [[] for _ in range(n + 1)]
	colors = [-1] + list(map(int, input().split()))
	for _ in range(n - 1):
		u, v = map(int, input().split())
		adj[u].append(v)
		adj[v].append(u)

	color_dp = [0 for _ in range(n + 1)]
	order, parent = get_order_parent(adj, n)
	# Final summation
	res = 0
	for c in set(colors):
		if c < 1: continue
		res = (res + iterative_dfs(n, colors, c, order, parent)) % MOD
	print(res)


solve()
