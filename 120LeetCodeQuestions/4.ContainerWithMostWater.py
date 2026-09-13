## You are given an integer array height of length n. 
## There are n vertical lines drawn 
## such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
## Find two lines that together with the x-axis form a container, such that the container contains the most water.
## Return the maximum amount of water a container can store.
## Notice that you may not slant the container.

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        area_max = 0
        area = 1
        while i < j:
            second = min(height[i],height[j])
            area = (j - i) * second
            if height[i] < height[j]:
                i += 1
            else:
                j -=1 
            area_max = max(area, area_max)
        return area_max