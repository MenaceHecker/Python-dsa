class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0

        unique = {}
        low = 0
        high = 0
        check = 0          # we'll use this as max frequency in the window
        ini_check = 0      # unused, kept to avoid "significant change"
        l = 0

        while high < len(s):
            c = s[high]
            unique[c] = unique.get(c, 0) + 1
            if unique[c] > check:
                check = unique[c]

            # if window needs more than k replacements, shrink from left
            while (high - low + 1) - check > k:
                left = s[low]
                unique[left] -= 1
                low += 1

            # update best length
            if (high - low + 1) > l:
                l = high - low + 1

            high += 1

        return l