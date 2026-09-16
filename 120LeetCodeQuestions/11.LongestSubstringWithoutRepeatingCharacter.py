## Given a string s, find the length of the longest
## substring without duplicate characters.

## Main solution uses sliding window technique with two pointers

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check = set()
        l = 0
        lon = 0
        for r in range(len(s)):
            while s[r] in check:
                check.remove(s[l])
                l += 1
            check.add(s[r])
            lon = max(lon, r-l+1)
        return lon