import random
class StringHashing:
	def __init__(self,s):
		self.s = s
		self.n = len(s)
		n = len(s)
		self.mod1 = 10**9 + 7
		self.mod2 = 10**9 + 9

		self.base = random.randint(10,10**7)

		self.h1 = [0 for _ in range(n+1)]
		self.h2 = [0 for _ in range(n+1)]
		self.p1 = [0 for _ in range(n+1)]
		self.p2 = [0 for _ in range(n+1)]
		