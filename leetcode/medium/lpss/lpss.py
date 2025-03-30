from pyparsing import empty


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Base Case
        substrings = [[] for i in range(len(s))]
        for i in range(len(s)):
            substrings[0].append((i,i))
            if i - 1 >= 0 and s[i - 1] == s[i]:
                substrings[1].append((i - 1, i))
        for i in range(2, len(s)):
            prev = i-2
            for pair in substrings[prev]:
                start = pair[0]-1
                end = pair[1]+1
                if (start > -1) and (end < len(s)):
                    if s[start] == s[end]:
                        substrings[i].append((start,end))
        palindrome = '';
        for i in range(1,len(s)):
            if len(substrings[i]) > 0:
                indices = substrings[i][0]
                palindrome = s[indices[0]:indices[1]+1]
        return palindrome



n = int(input())
for i in range(n):
    s = input()
    print(Solution().longestPalindrome(s))
