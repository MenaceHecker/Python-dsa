## Given a string s, 
## find the length of the longest substring without duplicate characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        low = 0
        high = 0
        count = 0
        uni = set()
        while high < len(s):
            if s[high] not in uni:
                uni.add(s[high])
                high += 1
                count = max(count, high - low)
            else:
                uni.remove(s[low])  
                low += 1 
        return count




        