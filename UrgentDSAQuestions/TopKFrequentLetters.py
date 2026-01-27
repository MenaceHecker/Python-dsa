## Given an integer array nums and an integer k, return the k most frequent elements.
## You may return the answer in any order.

import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c=Counter(nums)
        b=[[] for _ in range(len(nums)+1)]
        for n in nums:
            val=c[n]
            b[val].append(n)
        l=set()
        for j in range(len(nums),-1,-1):
            for n in b[j]:
                l.add(n)
                if len(l)==k:
                    return list(l)
        return list(l)
                



        