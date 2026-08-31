## Simple merge sort implementation in Python

import unittest
from typing import List


def merge(left: List[int], right: List[int]) -> List[int]:
    sorted_list = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list


def merge_sort(nums: List[int]) -> List[int]:
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])

    return merge(left, right)


class TestMergeSort(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(merge_sort([]), [])

    def test_single_item(self):
        self.assertEqual(merge_sort([5]), [5])

    def test_unsorted_list(self):
        self.assertEqual(merge_sort([3, 1, 4, 2]), [1, 2, 3, 4])

    def test_already_sorted_list(self):
        self.assertEqual(merge_sort([1, 2, 3, 4]), [1, 2, 3, 4])

    def test_duplicates(self):
        self.assertEqual(merge_sort([4, 1, 3, 1, 4]), [1, 1, 3, 4, 4])

    def test_negative_numbers(self):
        self.assertEqual(merge_sort([0, -3, 7, -1, 2]), [-3, -1, 0, 2, 7])

    def test_original_list_is_not_changed(self):
        nums = [3, 1, 2]
        self.assertEqual(merge_sort(nums), [1, 2, 3])
        self.assertEqual(nums, [3, 1, 2])

    def test_merge_two_sorted_lists(self):
        self.assertEqual(merge([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6])


if __name__ == "__main__":
    unittest.main()
