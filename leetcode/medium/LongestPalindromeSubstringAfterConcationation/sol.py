from typing import List


class Solution:
	def longestPalindrome(self, s: str, t: str) -> int:
		s_aps = []
		t_aps = []
		m = 1
		# Check in the string itself
		temp = self.lP(s)
		m = max(m, len(temp))
		temp = self.lP(t)
		m = max(m, len(temp))
		# create all possible substrings
		for i in range(len(s)):
			for j in range(i,len(s)):
				s_aps.append(s[i:j+1])
		for i in range(len(t)):
			for j in range(i,len(t)):
				t_aps.append(t[i:j+1])
		# Finds palindromes in all combinations of substrings
		for sub_s in s_aps:
			for sub_t in t_aps:
				if self.IsPalindrome(sub_s, sub_t):
					m = max(m, len(sub_s) + len(sub_t))
		return m

	def lP(self, s: str) -> List[str]:
		# Base Case
		substrings = [[] for i in range(len(s))]
		for i in range(len(s)):
			substrings[0].append((i, i))
			if i - 1 >= 0 and s[i - 1] == s[i]:
				substrings[1].append((i - 1, i))
		for i in range(2, len(s)):
			prev = i - 2
			for pair in substrings[prev]:
				start = pair[0] - 1
				end = pair[1] + 1
				if (start > -1) and (end < len(s)):
					if s[start] == s[end]:
						substrings[i].append((start, end))
		palindrome = '';
		for i in range(1, len(s)):
			if len(substrings[i]) > 0:
				indices = substrings[i][0]
				palindrome = s[indices[0]:indices[1] + 1]
		return palindrome

	def IsPalindrome(self, s: str, t: str) -> bool:
		concat = s + t
		for i in range(len(concat) // 2):
			if concat[i] != concat[-i - 1]:
				return False
		return True


sol = Solution()
#print(sol.longestPalindrome('a', 'a'))
#print(sol.longestPalindrome('abc', 'def'))
print(sol.longestPalindrome("wfkylwugfmfbmw",
"owncnoxsooekzficokxyg",))