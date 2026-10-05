## Given an array nums of n integers where nums[i] is in the range [1, n], 
## return an array of all the integers in the range [1, n] that do not appear in nums.

class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        check = set()
        result = []
        j = 1
        for i in nums:
            if i in check:
                continue
            check.add(i)
        while j <= len(nums):
            if j not in check:
                result.append(j)
            j += 1
        return result 

        