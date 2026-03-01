## Given an integer array nums, return true if any value appears at least twice in the array, 
## and return false if every element is distinct.

from ast import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        checked = set()
        for i in nums:
            if i in checked:
                return True
            checked.add(i)
        return False