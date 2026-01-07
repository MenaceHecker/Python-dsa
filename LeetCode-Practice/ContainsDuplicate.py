## Working solution but time exceeded on leetcode
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        val = 0
        check = 0
        i = 0
        length = len(nums)
        while (i<length):
            val = nums[i]
            j = i + 1
            while (j<length):
                check = nums[j]
                if (val == check):
                    return True
                j +=1 
            i += 1
        return False
    
## Optimal solution using set
## set an unordered collection of unique and immutable elements
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        checked = set()
        for i in nums:
            if i in checked:
                return True
            checked.add(i)
        return False