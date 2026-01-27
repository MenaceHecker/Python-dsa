## Given a string s, find the length of the longest
## substring without duplicate characters.
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
