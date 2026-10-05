## Given an array nums containing n distinct numbers in the range [0, n], 
## return the only number in the range that is missing from the array.

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        check = set()
        checked = []
        j = 0
        for i in nums:
            if i in check:
                continue
            check.add(i)
        while j <= len(nums):
            checked.append(j)
            if j not in check:
                return j
            j += 1
        return -1

        