## Simple quick sort implementation in Python
## Purely functional approach without in-place sorting

from typing import List


class Solution:
    def partition(self, nums: List[int], low: int, high: int) -> int:
        pivot = nums[high]
        i = low - 1

        for j in range(low, high):
            if nums[j] < pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]

        nums[i + 1], nums[high] = nums[high], nums[i + 1]
        return i + 1

    def quickSort(self, nums: List[int], low: int, high: int) -> List[int]:
        if low >= high:
            return
        pivot_index = self.partition(nums, low, high)
        self.quickSort(nums, low, pivot_index - 1)
        self.quickSort(nums, pivot_index + 1, high)

        quickSort(nums, 0, len(nums) - 1)
        return nums