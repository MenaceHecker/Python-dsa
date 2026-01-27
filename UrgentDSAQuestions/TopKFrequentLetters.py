## Given an integer array nums and an integer k, return the k most frequent elements.
## You may return the answer in any order.

import heapq
from collections import Counter
from typing import List
import unittest

## Main Solution
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c=Counter(nums)
        b=[[] for _ in range(len(nums)+1)]
        for n in nums:
            val=c[n]
            b[val].append(n)
        l=set()
        for j in range(len(nums),-1,-1):
            for n in b[j]:
                l.add(n)
                if len(l)==k:
                    return list(l)
        return list(l)








 ## Test functions               
def _assert_top_k(testcase: unittest.TestCase, nums: List[int], k: int, actual: List[int]) -> None:
    counts = Counter(nums)
    sorted_freqs = sorted(counts.values(), reverse=True)
    kth_freq = sorted_freqs[k - 1]
    top_k_by_freq = {n for n, freq in counts.items() if freq > kth_freq}
    candidates_at_k = {n for n, freq in counts.items() if freq == kth_freq}

    actual_set = set(actual)
    testcase.assertEqual(len(actual_set), k)
    testcase.assertTrue(top_k_by_freq.issubset(actual_set))
    testcase.assertTrue(actual_set.issubset(top_k_by_freq | candidates_at_k))


class TestTopKFrequent(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_basic_case(self):
        nums = [1, 1, 1, 2, 2, 3]
        k = 2
        actual = self.solution.topKFrequent(nums, k)
        _assert_top_k(self, nums, k, actual)

    def test_single_element(self):
        nums = [4]
        k = 1
        actual = self.solution.topKFrequent(nums, k)
        self.assertEqual(set(actual), {4})

    def test_with_ties_at_boundary(self):
        nums = [1, 1, 2, 2, 3, 3]
        k = 2
        actual = self.solution.topKFrequent(nums, k)
        _assert_top_k(self, nums, k, actual)

    def test_with_negative_numbers(self):
        nums = [-1, -1, -2, -3, -3, -3]
        k = 2
        actual = self.solution.topKFrequent(nums, k)
        _assert_top_k(self, nums, k, actual)

    def test_all_same_frequency(self):
        nums = [5, 6, 7, 8]
        k = 3
        actual = self.solution.topKFrequent(nums, k)
        self.assertEqual(len(set(actual)), 3)
        self.assertTrue(set(actual).issubset(set(nums)))


if __name__ == "__main__":
    unittest.main()
