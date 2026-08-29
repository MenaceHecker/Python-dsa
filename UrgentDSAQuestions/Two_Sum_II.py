## Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, 
## find two numbers such that they add up to a specific target number.


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums = {}
        dif = 0
        l = len(numbers)
        i = 0
        result = []
        while i < l:
            dif = target - numbers[i]
            if dif in nums:
                result.append(nums[dif]+1)
                result.append(i+1)
                return result
            nums[numbers[i]] = i    
            i += 1


        