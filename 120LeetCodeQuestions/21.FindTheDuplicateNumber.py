## Given an array of integers nums containing n + 1 integers 
## where each integer is in the range [1, n] inclusive.
## There is only one repeated number in nums, return this repeated number.
## You must solve the problem without modifying the array nums and using only constant extra space.

class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        check = set()
        for i in nums:
            if i in check:
                return i
            check.add(i)
        return -1
        