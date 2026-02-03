## Given an array of integers nums and an integer target, 
## return indices of the two numbers such that they add up to target.

from typing import List
import unittest

## Main Solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        dif = 0
        sol = []
        for i in range(len(nums)):
            my_dict[nums[i]] = i
         
        for i in range (len(nums)):
            dif = target - nums[i]
            if dif in my_dict and my_dict[dif] != i:
                return [i, my_dict[dif]]

        return []












 ## Test functions
class TestTwoSum(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_basic_case(self):
        self.assertEqual(self.solution.twoSum([2, 7, 11, 15], 9), [0, 1])

    def test_with_duplicates(self):
        self.assertEqual(self.solution.twoSum([3, 3], 6), [0, 1])

    def test_with_zeroes(self):
        self.assertEqual(self.solution.twoSum([0, 4, 3, 0], 0), [0, 3])

    def test_with_negative_numbers(self):
        self.assertEqual(self.solution.twoSum([-1, -2, -3, -4, -5], -8), [2, 4])

    def test_no_solution(self):
        self.assertEqual(self.solution.twoSum([1, 2, 3], 100), [])


if __name__ == "__main__":
    unittest.main()
