## Write an algorithm to determine if a number n is happy.
## A happy number is a number defined by the following process:
## Starting with any positive integer, replace the number by the sum of the squares of its digits.
## Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
## Those numbers for which this process ends in 1 are happy.
## Return true if n is a happy number, and false if not.

## Implementation with set approach
class Solution:
    def isHappy(self, n: int) -> bool:
        num = n
        tot = 0
        seen = set()
        while num != 1:
            if num in seen:
                return False
            seen.add(num)
            while num != 0:
                digit = num % 10
                tot = tot + (digit * digit)
                num = num // 10
            num = tot
            tot = 0
        return True


