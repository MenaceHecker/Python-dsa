## Given an array of strings strs, group the anagrams together.
## You can return the answer in any order.

from typing import List
import unittest

## Main Solution
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            wordSorted = "".join(sorted(s))
            if wordSorted not in groups:
                groups[wordSorted] = []
            groups[wordSorted].append(s)
        return list(groups.values())











##Test functions
def _normalize(groups: List[List[str]]) -> List[List[str]]:
    """Sort within groups and across groups so order doesn't affect tests."""
    return sorted([sorted(group) for group in groups])


class TestGroupAnagrams(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_case(self):
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        expected = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
        actual = self.solution.groupAnagrams(strs)
        self.assertEqual(_normalize(actual), _normalize(expected))

    def test_empty_input(self):
        self.assertEqual(self.solution.groupAnagrams([]), [])

    def test_single_empty_string(self):
        self.assertEqual(self.solution.groupAnagrams([""]), [[""]])

    def test_no_anagrams(self):
        strs = ["abc", "def", "ghi"]
        expected = [["abc"], ["def"], ["ghi"]]
        actual = self.solution.groupAnagrams(strs)
        self.assertEqual(_normalize(actual), _normalize(expected))

    def test_with_duplicates(self):
        strs = ["ab", "ba", "ab"]
        expected = [["ab", "ab", "ba"]]
        actual = self.solution.groupAnagrams(strs)
        self.assertEqual(_normalize(actual), _normalize(expected))


if __name__ == "__main__":
    unittest.main()
