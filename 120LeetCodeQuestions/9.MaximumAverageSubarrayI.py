## You are given an integer array nums consisting of n elements, and an integer k.
## Find a contiguous subarray whose length is equal to k 
## that has the maximum average value and return this value. 

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_sum = window_sum
        for i in range(k,len(nums)):
            window_sum += nums[i]
            window_sum -= nums[i-k]
            max_sum = max(max_sum, window_sum)
        avg = max_sum / k
        return avg
