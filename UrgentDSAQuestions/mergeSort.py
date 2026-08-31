## Simple merge sort implementation in Python

from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(nums):
            # Base case
            if len(nums) <= 1:
                return nums

            # Split
            mid = len(nums) // 2

            left = nums[:mid]
            right = nums[mid:]

            # Recursively sort both halves
            left = mergeSort(left)
            right = mergeSort(right)

            # Merge
            result = []
            i = 0
            j = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1

            # Add leftovers
            result.extend(left[i:])
            result.extend(right[j:])

            return result
        return mergeSort(nums)
