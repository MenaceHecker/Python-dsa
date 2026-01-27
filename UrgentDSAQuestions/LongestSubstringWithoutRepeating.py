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




## Unit tests for Longest Substring Without Repeating Characters
import unittest


class TestLongestSubstringWithoutRepeating(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_examples(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("abcabcbb"), 3)
        self.assertEqual(self.solution.lengthOfLongestSubstring("bbbbb"), 1)
        self.assertEqual(self.solution.lengthOfLongestSubstring("pwwkew"), 3)

    def test_empty_string(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring(""), 0)

    def test_single_char_and_all_unique(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("a"), 1)
        self.assertEqual(self.solution.lengthOfLongestSubstring("abcdef"), 6)

    def test_repeats_and_overlaps(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("abba"), 2)
        self.assertEqual(self.solution.lengthOfLongestSubstring("dvdf"), 3)
        self.assertEqual(self.solution.lengthOfLongestSubstring("tmmzuxt"), 5)

    def test_whitespace(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring(" "), 1)
        self.assertEqual(self.solution.lengthOfLongestSubstring("a b a"), 3)


if __name__ == "__main__":
    unittest.main()
